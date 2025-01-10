from contextlib import asynccontextmanager

from fastapi import FastAPI

from small_service.content.router import router as content_router
from small_service.utils import create_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize db."""
    create_tables()
    yield


app = FastAPI(
    lifespan=lifespan,
    title="Small API to store some content as string",
)

app.include_router(content_router)
