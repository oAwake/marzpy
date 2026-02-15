from dataclasses import dataclass, field
from typing import Optional, Dict, Any, List


# =========================================================
# Model
# =========================================================

@dataclass
class User:
    username: str
    proxies: Dict[str, Any]
    inbounds: Dict[str, Any]
    data_limit: float

    data_limit_reset_strategy: str = "no_reset"
    status: str = ""
    expire: float = 0
    used_traffic: int = 0
    lifetime_used_traffic: int = 0
    created_at: Optional[str] = None

    links: List[str] = field(default_factory=list)
    subscription_url: str = ""
    excluded_inbounds: Dict[str, Any] = field(default_factory=dict)

    note: str = ""
    on_hold_timeout: int = 0
    on_hold_expire_duration: int = 0
    sub_updated_at: int = 0
    online_at: int = 0
    sub_last_user_agent: str = ""
    admin: str = ""

    auto_delete_in_days: Optional[int] = None
    next_plan: Optional[Dict[str, Any]] = None


# =========================================================
# Methods (internal auth system)
# =========================================================

class UserMethods:

    # -------------------------------------------
    # Create
    # -------------------------------------------
    def add_user(self, user: User) -> User:
        user.status = "active"
        if user.on_hold_expire_duration:
            user.status = "on_hold"

        data = self._request(
            "POST",
            "/user",
            json_data=user.__dict__,
        )
        return User(**data)

    # -------------------------------------------
    # Get One
    # -------------------------------------------
    def get_user(self, username: str) -> User:
        data = self._request(
            "GET",
            f"/user/{username}",
        )
        return User(**data)

    # -------------------------------------------
    # Update
    # -------------------------------------------
    def modify_user(self, username: str, user: User) -> User:
        data = self._request(
            "PUT",
            f"/user/{username}",
            json_data=user.__dict__,
        )
        return User(**data)

    # -------------------------------------------
    # Delete
    # -------------------------------------------
    def delete_user(self, username: str) -> str:
        self._request("DELETE", f"/user/{username}")
        return "success"

    # -------------------------------------------
    # Reset Traffic
    # -------------------------------------------
    def reset_user_traffic(self, username: str) -> str:
        self._request("POST", f"/user/{username}/reset")
        return "success"

    # -------------------------------------------
    # Revoke Subscription
    # -------------------------------------------
    def revoke_sub(self, username: str) -> User:
        data = self._request("POST", f"/user/{username}/revoke_sub")
        return User(**data)

    # -------------------------------------------
    # List Users (clean query builder)
    # -------------------------------------------
    def get_all_users(
        self,
        username: Optional[str] = None,
        status: Optional[str] = None,
        search: Optional[str] = None,
    ) -> List[User]:

        params = {}

        if username:
            params["username"] = username
        if search:
            params["search"] = search
        if status:
            params["status"] = status

        data = self._request("GET", "/users", params=params)

        return [User(**u) for u in data.get("users", [])]

    # -------------------------------------------
    # Reset All
    # -------------------------------------------
    def reset_all_users_traffic(self) -> str:
        self._request("POST", "/users/reset")
        return "success"

    # -------------------------------------------
    # Usage
    # -------------------------------------------
    def get_user_usage(self, username: str) -> Dict[str, Any]:
        data = self._request("GET", f"/user/{username}/usage")
        return data.get("usages", {})

    # -------------------------------------------
    # Count
    # -------------------------------------------
    def get_all_users_count(self) -> int:
        data = self._request("GET", "/users")
        return data.get("content", {}).get("total", 0)
