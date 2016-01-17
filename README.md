OU Price Picker
=================
Provide price recommendations for products based on product name and (optional) location

Dependencies:
=======
- Python 3.5
- aiohttp
- aiopg

request format: 
http://<service>/item-price-service/?item=<item name>&city=<city name>
item param is required, city is optional.

200/OK response format: 
{
   "status": <http status>,
   "content": {
     "item": <item name>,
     "item_count": <total row count for item>,
     "price_suggestion": <recommended price,
     "city": <city name or "Not specified">
    }
}

404/Not found response format:
{
  "status": <http status>,
  "content": {
    "message": <message>
    }
}

500/Server Error response format:
{
  "status": <http status>,
  "content": {
    "message": <message>,
    "trace": <trace content>
    }
}
