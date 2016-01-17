from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options

from ousvc.config import Config

cache_opts = {
    'cache.type': 'memory'
}

cache = CacheManager(**parse_cache_config_options(cache_opts))

config = Config.get_config()
cache_name = 'oucache'
cache_enabled = config.cache_enabled
cache_exp = config.cache_timeout


class Cache:
    @staticmethod
    def get_record(title, city):
        if cache_enabled:
            tmpcache = cache.get_cache(cache_name, expire=cache_exp)
            key = title + str(city)
            if key in tmpcache:
                return tmpcache[key]
        return None

    @staticmethod
    def set_record(title, city, record):
        if cache_enabled:
            tmpcache = cache.get_cache(cache_name, expire=cache_exp)
            key = title + str(city)
            tmpcache[key] = record
