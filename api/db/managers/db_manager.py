from aiopg.sa import create_engine, Engine


class DbManager:
    db: Engine = None

    @classmethod
    async def connect_db(cls, app):
        cls.db = await create_engine(
            database='contacts',
            user='contacts_api',
            password='qdg058znm230',
            host='127.0.0.1',
            port='5432',
            minsize=1,
            maxsize=5
        )

    @classmethod
    async def close_db(cls, app):
        cls.db.close()
        await cls.db.wait_closed()

    @staticmethod
    async def query_record(operation) -> dict:
        async with DbManager.db.acquire() as conn:
            cursor = await conn.execute(operation)
            result = await cursor.fetchone()
        return result

    @staticmethod
    async def query_list(operation) -> list:
        async with DbManager.db.acquire() as conn:
            cursor = await conn.execute(operation)
            result = await cursor.fetchall()
        return result

    @staticmethod
    async def query_scalar(operation) -> int:
        async with DbManager.db.acquire() as conn:
            cursor = await conn.execute(operation)
            result = await cursor.scalar()
        return result

    @staticmethod
    async def query(operation) -> None:
        async with DbManager.db.acquire() as conn:
            await conn.execute(operation)
