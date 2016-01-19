import configparser


class Data:
    instance = None


class Config:
    @staticmethod
    def get_config():
        if Data.instance is None:
            instance = Config()
            cfg = configparser.ConfigParser()
            cfg.read('config/config.ini')
            info = cfg['DbConnectionInfo']
            host = info['Host']
            dbname = info['DbName']
            user = info['User']
            password = info['Password']
            instance.tablename = info['TableName']
            instance.cache_enabled = info.getboolean('EnableCache')
            instance.cache_server = info['MemcachedServer']
            instance.dsn = "host='{host}' dbname='{name}' user='{user}' password='{password}'" \
                .format(host=host, name=dbname, user=user, password=password)
            Data.instance = instance
        return Data.instance
