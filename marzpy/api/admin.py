class Admin:
    def __init__(self, username: str, password: str, panel_address: str):
        self.username = username
        self.password = password
        self.panel_address = panel_address

    # ---------------------------
    # Admin Info
    # ---------------------------

    def get_current_admin(self):
        return self._request("GET", "admin")

    # ---------------------------
    # Create
    # ---------------------------

    def create_admin(self, data: dict):
        self._request("POST", "admin", json_data=data)
        return "success"

    # ---------------------------
    # Change Password
    # ---------------------------

    def change_admin_password(self, username: str, data: dict):
        self._request("PUT", f"admin/{username}", json_data=data)
        return "success"

    # ---------------------------
    # Delete
    # ---------------------------

    def delete_admin(self, username: str):
        self._request("DELETE", f"admin/{username}")
        return "success"

    # ---------------------------
    # List
    # ---------------------------

    def get_all_admins(self):
        return self._request("GET", "admins")
