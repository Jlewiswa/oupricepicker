from ousvc.config import Config

config = Config.get_config()

list_price_select = \
    "WITH offer AS (SELECT list_price AS price FROM {0} \
    WHERE title = %(title)s {1}), \
    rowcount AS (SELECT count(price) AS total FROM offer) \
    SELECT price, total, count(price) AS qty FROM offer, rowcount \
    GROUP BY price, total ORDER BY qty DESC, price DESC LIMIT 1"

# alternative query option, may offer price recommendations that better indicate market value.
# return sell price if available, otherwise list price
sell_price_weighted_select = \
    "WITH offer AS (SELECT CASE WHEN sell_price != Null THEN sell_price ELSE list_price END AS price FROM {0} \
    WHERE title = %(title)s {1}), \
    rowcount AS (SELECT count(price) AS total FROM offer) \
    SELECT price, total, count(price) AS qty FROM offer, rowcount \
    GROUP BY price, total ORDER BY qty DESC, price DESC LIMIT 1"

city_clause = "AND city = %(city)s"


class Queries:
    @staticmethod
    def get_sellprice_select(title, city):
        return Queries.get_select(sell_price_weighted_select, title, city)

    @staticmethod
    def get_listprice_select(title, city):
        return Queries.get_select(list_price_select, title, city)

    @staticmethod
    def get_select(select, title, city):
        params = {'title': title}
        city_str = ""
        if city is not None:
            city_str = city_clause
            params['city'] = city
        query = select.format(config.tablename, city_str)
        return query, params
