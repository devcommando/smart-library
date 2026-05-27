from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from ..config import settings

# Database connection pool
db_engine = create_async_engine(settings.database_url)
async_session_factory = sessionmaker(bind=db_engine,class_=AsyncSession,expire_on_commit=False)

async def get_db():
    async with async_session_factory() as session:
        yield session

