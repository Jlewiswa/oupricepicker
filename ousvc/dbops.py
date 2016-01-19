import aiopg
from ousvc.cache import Cache
from ousvc.config import Config
from ousvc.queries import Queries


class Pool:
    pool = None


# Database operations. Receives validated title and city from process_data
# and uses these values to query the database. Responsible for returning
# a valid array with price & count, or None if no record is available.
# With cache enabled, attempts to first retrieve a cached record.
class DbOps:
    @staticmethod
    async def get_connection_pool():
        if Pool.pool is None:
            config = Config.get_config()
            Pool.pool = await aiopg.create_pool(config.dsn)
        return Pool.pool

    @staticmethod
    async def get_price(title, city=None):
        record = Cache.get_record(title, city)
        if record is None:
            pool = await DbOps.get_connection_pool()
            async with pool.acquire() as conn:
                async with conn.cursor() as cursor:
                    query, params = Queries.get_listprice_select(title, city)
                    await cursor.execute(query, params)
                    record = await cursor.fetchone()
                    Cache.set_record(title, city, record)
        return record
