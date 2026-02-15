from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Node:
    name: str
    address: str
    port: int
    api_port: int
    certificate: str
    id: int
    xray_version: Optional[str] = None
    status: Optional[str] = None
    message: Optional[str] = None


class NodeMethods:
    # ----------------------------------------
    # Create
    # ----------------------------------------
    def add_node(self, node: Node) -> Node:
        data = self._request(
            "POST",
            "node",
            json_data=node.__dict__,
        )
        return Node(**data)

    # ----------------------------------------
    # Read
    # ----------------------------------------
    def get_node_by_id(self, node_id: int) -> Node:
        data = self._request("GET", f"node/{node_id}")
        return Node(**data)

    def get_all_nodes(self) -> List[Node]:
        data = self._request("GET", "nodes")
        return [Node(**node) for node in data]

    # ----------------------------------------
    # Update
    # ----------------------------------------
    def modify_node_by_id(self, node_id: int, node: Node) -> Node:
        data = self._request(
            "PUT",
            f"node/{node_id}",
            json_data=node.__dict__,
        )
        return Node(**data)

    # ----------------------------------------
    # Delete
    # ----------------------------------------
    def delete_node(self, node_id: int) -> str:
        self._request("DELETE", f"node/{node_id}")
        return "success"

    # ----------------------------------------
    # Actions
    # ----------------------------------------
    def reconnect_node(self, node_id: int) -> str:
        self._request("POST", f"node/{node_id}/reconnect")
        return "success"

    def get_nodes_usage(self):
        data = self._request("GET", "nodes/usage")
        return data.get("usages", [])
