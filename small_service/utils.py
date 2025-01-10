from small_service.content.models import Content
from small_service.database import engine


def create_tables():
    """
    Creates all database tables defined in the application.
    """
    Content.metadata.create_all(bind=engine)
