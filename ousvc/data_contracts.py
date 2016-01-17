import json


class DataContracts:
    @staticmethod
    def get_oudemo_200(item, count, price, city=None):
        status = 200
        city_text = "Not Specified" if city is None else city
        # OrderedDict?
        return json.dumps({
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
        return json.dumps({
            "status": status,
            "content": {
                "message": message}
        })

    @staticmethod
    def get_500(trace):
        status = 500
        message = "A server error occurred"
        return json.dumps({
            "status": status,
            "content": {
                "message": message,
                "trace": str(trace)
            }
        })