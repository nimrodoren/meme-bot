from datetime import datetime

from pydantic import BaseModel, AnyHttpUrl

from enums.hook_types import HookType

class Delieverables(BaseModel):
    id: int
    guid: str
    delivered_at: datetime
    status: str
    event: str

class Hook(BaseModel):
    hook_type: HookType
    name: str
    active: bool
    events: list[str]
    url: AnyHttpUrl
    deliverable_list: list[Delieverables]

