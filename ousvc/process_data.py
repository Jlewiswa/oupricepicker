from ousvc.data_contracts import DataContracts
from ousvc.dbops import DbOps


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
