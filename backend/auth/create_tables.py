import asyncio
from database.base import Base
from database.session import engine
from sqlalchemy import inspect

from auth.app.models import User

async def create_db_and_tables():
    print ("connecting to database: ", str(engine.url))
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        def inspect_tables(sync_conn):
            inspector = inspect(sync_conn)
            return inspector.get_table_names()

        tables = await conn.run_sync(inspect_tables)
        print("Tables in the database:", tables)
    print("Database and tables created successfully.")

if __name__ == "__main__":
    asyncio.run(create_db_and_tables())