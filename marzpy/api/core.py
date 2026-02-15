class Core:
    def get_xray_core(self):
        """
        Get Xray core status
        """
        return self._request("GET", "/core")

    def restart_xray_core(self):
        """
        Restart Xray core
        """
        self._request("POST", "/core/restart")
        return "success"

    def get_xray_config(self):
        """
        Get Xray config
        """
        return self._request("GET", "/core/config")

    def modify_xray_config(self, config: dict):
        """
        Update Xray config
        """
        self._request("PUT", "/core/config", json_data=config)
        return "success"
