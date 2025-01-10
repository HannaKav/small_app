from uuid import UUID

from pydantic import BaseModel, ConfigDict

__all__ = ["ContentOutput"]


class BaseSchemaModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class ContentOutput(BaseSchemaModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    value: str
