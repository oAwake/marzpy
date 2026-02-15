import base64
import httpx
from typing import Optional, Dict, Any


class Subscription:
    def __init__(self, timeout: int = 15):
        self.client = httpx.Client(
            http2=True,
            timeout=httpx.Timeout(timeout),
            limits=httpx.Limits(
                max_connections=20,
                max_keepalive_connections=10,
            ),
        )

    # --------------------------------------------------
    # Internal request
    # --------------------------------------------------
    def _sub_request(self, sub_link: str, endpoint: str = ""):
        url = f"{sub_link.rstrip('/')}/{endpoint}".rstrip("/")

        try:
            response = self.client.get(
                url,
                headers={"Accept": "application/json"},
            )

            response.raise_for_status()

            # اگر endpoint داشت → JSON
            if endpoint:
                return response.json()

            # اگر endpoint نداشت → base64 subscription
            decoded = base64.b64decode(response.content)
            return decoded.decode("utf-8")

        except httpx.HTTPStatusError as e:
            raise Exception(
                f"Subscription HTTP error {e.response.status_code}: {e.response.text}"
            )
        except Exception as e:
            raise Exception(f"Subscription error: {str(e)}")

    # --------------------------------------------------
    # Public methods
    # --------------------------------------------------
    def get_subscription(self, sub_link: str) -> str:
        """
        Returns decoded subscription string (base64 decoded)
        """
        return self._sub_request(sub_link)

    def get_subscription_info(self, sub_link: str) -> Dict[str, Any]:
        """
        Returns subscription metadata JSON
        """
        return self._sub_request(sub_link, "info")
