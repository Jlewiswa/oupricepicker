from ousvc.process_data import Process
from urllib.parse import parse_qsl
from aiohttp import web, MultiDict


class PriceService:
    @staticmethod
    async def oudemo(request):
        get_params = MultiDict(parse_qsl(request.query_string))
        status, result = await Process.process(get_params)
        return web.Response(text=result, content_type="application/json", status=status)


app = web.Application()
app.router.add_route("GET", "/item-price-service/", PriceService.oudemo)
