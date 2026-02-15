from dataclasses import dataclass, field
from typing import Optional, Dict, Any


# =========================================================
# Model
# =========================================================

@dataclass
class Template:
    name: str = ""
    inbounds: Dict[str, Any] = field(default_factory=dict)
    data_limit: Dict[str, Any] = field(default_factory=dict)
    expire_duration: int = 0
    username_prefix: str = ""
    username_suffix: str = ""
    id: Optional[int] = None


# =========================================================
# Methods (internal token system)
# =========================================================

class TemplateMethods:

    # -------------------------------------------
    # Get All
    # -------------------------------------------
    def get_all_templates(self):
        data = self._request("GET", "/user_template")
        return [Template(**t) for t in data]

    # -------------------------------------------
    # Create
    # -------------------------------------------
    def add_template(self, template: Template):
        data = self._request(
            "POST",
            "/user_template",
            json_data=template.__dict__,
        )
        return Template(**data)

    # -------------------------------------------
    # Get By ID
    # -------------------------------------------
    def get_template_by_id(self, template_id: int):
        data = self._request(
            "GET",
            f"/user_template/{template_id}",
        )
        return Template(**data)

    # -------------------------------------------
    # Update
    # -------------------------------------------
    def modify_template_by_id(self, template_id: int, template: Template):
        data = self._request(
            "PUT",
            f"/user_template/{template_id}",
            json_data=template.__dict__,
        )
        return Template(**data)

    # -------------------------------------------
    # Delete
    # -------------------------------------------
    def delete_template_by_id(self, template_id: int):
        self._request(
            "DELETE",
            f"/user_template/{template_id}",
        )
        return "success"
