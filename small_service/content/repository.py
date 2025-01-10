from typing import Type
from uuid import UUID

from sqlalchemy.orm import Session

from .models import Content


class ContentRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, value: str) -> Content:
        content = Content(value=value)
        self.session.add(content)
        self.session.commit()
        self.session.refresh(content)
        return content

    def update(self, content: Content, value: str) -> Content:
        content.value = value
        self.session.commit()
        self.session.refresh(content)
        return content

    def delete(self, content: Content) -> bool:
        self.session.delete(content)
        self.session.commit()
        return True

    def get_by_id(self, content_id: UUID) -> Content | None:
        content = self.session.query(Content).filter(Content.id == content_id).first()
        return content

    def list(self) -> list[Type[Content]]:
        return self.session.query(Content).all()
