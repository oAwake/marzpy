class System:
    # --------------------------------------------------
    # System Stats
    # --------------------------------------------------
    def get_system_stats(self):
        """
        Returns server stats
        """
        return self._request("GET", "/system")

    # --------------------------------------------------
    # Inbounds
    # --------------------------------------------------
    def get_inbounds(self):
        """
        Returns server inbounds
        """
        return self._request("GET", "/inbounds")

    # --------------------------------------------------
    # Hosts
    # --------------------------------------------------
    def get_hosts(self):
        """
        Returns server hosts
        """
        return self._request("GET", "/hosts")

    def modify_hosts(self, data: dict):
        """
        Updates server hosts
        """
        return self._request("PUT", "/hosts", json=data)
