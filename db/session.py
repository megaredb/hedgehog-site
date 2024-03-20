from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from config import DATABASE_URL
from contextlib import asynccontextmanager
from logging import error
from typing import AsyncGenerator

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker


async_engine: AsyncEngine = create_async_engine(
    DATABASE_URL,
    future=True,
)


@asynccontextmanager
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async_session = sessionmaker(  # noqa
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as async_sess:
        try:
            yield async_sess

        except SQLAlchemyError as e:
            error("An error occurred while trying to create an async session.")
            error(e)
