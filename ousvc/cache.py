from ousvc.config import Config
import pylibmc

config = Config.get_config()
cache_enabled = config.cache_enabled
cache_server = config.cache_server


class Cache:
    @staticmethod
    def get_record(title, city):
        if cache_enabled:
            tmpcache = Cache.get_client()
            key = title + str(city)
            if key in tmpcache:
                return tmpcache.get(key)
        return None

    @staticmethod
    def set_record(title, city, record):
        if cache_enabled:
            tmpcache = Cache.get_client()
            key = title + str(city)
            tmpcache[key] = record

    @staticmethod
    def get_client():
        return pylibmc.Client([cache_server], binary=True, behaviors={"tcp_nodelay": True, "ketama": True})
