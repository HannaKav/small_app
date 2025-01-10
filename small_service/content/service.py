from uuid import UUID

from fastapi import HTTPException
from sqlalchemy.orm import Session

from . import schemas
from .repository import ContentRepository


class ContentService:
    def __init__(self, session: Session):
        self.content_repository = ContentRepository(session)

    def create(self, value: str) -> schemas.ContentOutput:
        content = self.content_repository.create(value)
        return schemas.ContentOutput.model_validate(content)

    def update(self, content_id: UUID, value: str) -> schemas.ContentOutput:
        content = self.content_repository.get_by_id(content_id)
        if not content:
            raise HTTPException(status_code=404, detail="Content not found")

        updated_content = self.content_repository.update(content, value)
        return schemas.ContentOutput.model_validate(updated_content)

    def delete(self, content_id: UUID) -> bool:
        content = self.content_repository.get_by_id(content_id)
        if not content:
            raise HTTPException(status_code=404, detail="Content not found")

        return self.content_repository.delete(content)

    def get(self, content_id: UUID) -> schemas.ContentOutput:
        content = self.content_repository.get_by_id(content_id)
        if not content:
            raise HTTPException(status_code=404, detail="Content not found")

        return schemas.ContentOutput.model_validate(content)

    def list(self) -> list[schemas.ContentOutput]:
        content = self.content_repository.list()
        return [schemas.ContentOutput.model_validate(c) for c in content]
