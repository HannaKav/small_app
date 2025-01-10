from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from small_service.database import get_db

from .schemas import ContentOutput
from .service import ContentService

__all__ = ["router"]

router = APIRouter()


@router.post("/content", status_code=201)
def create_content(value: str, session: Session = Depends(get_db)) -> ContentOutput:
    service = ContentService(session)
    return service.create(value)


@router.put("/content/{content_id}", status_code=200)
def update_content(content_id: UUID, value: str, session: Session = Depends(get_db)) -> ContentOutput:
    service = ContentService(session)
    return service.update(content_id=content_id, value=value)


@router.delete("/content/{content_id}", status_code=204)
def delete_content(content_id: UUID, session: Session = Depends(get_db)) -> None:
    service = ContentService(session)
    service.delete(content_id)


@router.get("/content/{content_id}", status_code=200)
def get_content(content_id: UUID, session: Session = Depends(get_db)) -> ContentOutput:
    service = ContentService(session)
    return service.get(content_id)


@router.get("/content", status_code=200)
def list_content(session: Session = Depends(get_db)) -> list[ContentOutput]:
    service = ContentService(session)
    return service.list()
