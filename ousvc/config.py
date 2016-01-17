import configparser


class Data:
    instance = None


class Config:
    @staticmethod
    def get_config():
        if Data.instance is None:
            instance = Config()
            cfg = configparser.ConfigParser()
            cfg.read('../config/config.ini')
            info = cfg['DbConnectionInfo']
            host = info['Host']
            dbname = info['DbName']
            user = info['User']
            password = info['Password']
            instance.tablename = info['TableName']
            instance.dsn = "host='{}' dbname='{}' user='{}' password='{}'" \
                .format(host, dbname, user, password)
            Data.instance = instance
        return Data.instance
