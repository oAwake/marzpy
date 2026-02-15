import httpx
from typing import Optional, Dict, Any

from .admin import Admin
from .node import NodeMethods
from .subscription import Subscription
from .core import Core
from .user import UserMethods
from .template import TemplateMethods
from .system import System


class Methods(
    Admin,
    NodeMethods,
    Subscription,
    Core,
    UserMethods,
    TemplateMethods,
    System,
):
    def __init__(self, username: str, password: str, panel_address: str):
        self.username = username
        self.password = password
        self.panel_address = panel_address.rstrip("/")

        self._token_type: Optional[str] = None
        self._access_token: Optional[str] = None

        self._client = httpx.Client(
            http2=True,
            timeout=httpx.Timeout(20),
            limits=httpx.Limits(
                max_connections=100,
                max_keepalive_connections=50,
            ),
            headers={"accept": "application/json"},
        )

        self._login()

        super().__init__(username, password, panel_address)

    # =========================================================
    # Internal Auth
    # =========================================================

    def _login(self):
        response = self._client.post(
            f"{self.panel_address}/api/admin/token",
            data={
                "username": self.username,
                "password": self.password,
            },
            headers={
                "Content-Type": "application/x-www-form-urlencoded"
            },
        )

        response.raise_for_status()

        data = response.json()
        self._token_type = data["token_type"]
        self._access_token = data["access_token"]

    def _auth_headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"{self._token_type} {self._access_token}"
        }

    # =========================================================
    # Core Request Engine
    # =========================================================

    def _request(
        self,
        method: str,
        endpoint: str,
        json_data: Optional[Dict[str, Any]] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> Any:

        url = f"{self.panel_address}/api/{endpoint}"

        response = self._client.request(
            method,
            url,
            headers=self._auth_headers(),
            json=json_data,
            params=params,
        )

        # Auto relogin
        if response.status_code == 401:
            self._login()
            response = self._client.request(
                method,
                url,
                headers=self._auth_headers(),
                json=json_data,
                params=params,
            )

        response.raise_for_status()

        if response.content:
            return response.json()

        return None
