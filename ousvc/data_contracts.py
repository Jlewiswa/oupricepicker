import json


# Assembles json-formatted responses for available status codes.
class DataContracts:
    @staticmethod
    def get_oudemo_200(item, count, price, city=None):
        status = 200
        city_text = "Not specified" if city is None else city
        # OrderedDict?
        return status, json.dumps({
            "status": status,
            "content": {
                "item": item,
                "item_count": count,
                "price_suggestion": price,
                "city": city_text
            }
        })

    @staticmethod
    def get_oudemo_404():
        status = 404
        message = "Not found"
        return status, json.dumps({
            "status": status,
            "content": {
                "message": message}
        })

    @staticmethod
    def get_500(exc):
        status = 500
        message = "A server error occurred"
        return status, json.dumps({
            "status": status,
            "content": {
                "message": message,
                "trace": repr(exc)
            }
        })
