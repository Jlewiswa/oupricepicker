from ousvc.data_contracts import DataContracts
from ousvc.dbops import DbOps


# Data processing layer. Receives params from dispatcher, validates, then
# passes to dbops for db query. Responsible for returning a valid status code
# and json-formatted response body.
class Process:
    @staticmethod
    async def process(params):
        city = params.get('city')
        title = params.get('item')
        if title is None:
            return DataContracts.get_oudemo_404()

        try:
            record = await DbOps.get_price(title, city)
        except Exception as e:
            return DataContracts.get_500(e)
        if record is None:
            return DataContracts.get_oudemo_404()

        price = record[0]
        count = record[1]
        return DataContracts.get_oudemo_200(title, count, price, city)
