import aiopg
from ousvc.config import Config
from ousvc.queries import Queries


class Pool:
    pool = None


class DbOps:
    @staticmethod
    async def get_connection_pool():
        if Pool.pool is None:
            config = Config.get_config()
            Pool.pool = await aiopg.create_pool(config.dsn)
        return Pool.pool

    @staticmethod
    async def get_price(title, city=None):
        pool = await DbOps.get_connection_pool()
        async with pool.acquire() as conn:
            async with conn.cursor() as cursor:
                query, params = Queries.get_listprice_select(title, city)
                await cursor.execute(query, params)
                return await cursor.fetchone()
