import asyncio
import logging

import alembic.config
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_async_session

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def check():
    try:
        db: AsyncSession

        async with get_async_session() as db:
            await db.execute(text("SELECT 1"))
    except Exception as e:
        logger.error(e)
        raise e


def init() -> None:
    alembic_args = [
        "--raiseerr",
        "upgrade",
        "head",
    ]
    alembic.config.main(argv=alembic_args)

    asyncio.run(check())


def main() -> None:
    logger.info("Initializing service")
    init()
    logger.info("Service finished initializing")


if __name__ == "__main__":
    main()
