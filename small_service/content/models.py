import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from small_service.database import Base

__all__ = ["Content"]


class Content(Base):
    __tablename__ = "content"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    value = Column(String, nullable=False)
