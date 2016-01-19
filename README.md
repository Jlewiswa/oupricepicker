OU Price Picker
=================
Provide price recommendations for products based on product name and (optional) location

* Note: In the interest of presentation, I have intentionally employed various coding patterns 
throughout the project. I apologize for any resulting confusion.

Dependencies:
=======
- python 3.5
- postgresql
- memcached
- aiohttp
- aiopg
- pylibmc

request format: 
http://[host]/item-price-service/?item=[item name]&city=[city name]
item param is required, city is optional.

200/OK response format: 
{
   "status": [http status],
   "content": {
     "item": [item name],
     "item_count": [total row count for item],
     "price_suggestion": [recommended price],
     "city": [city name or "Not specified"]
    }
}

404/Not found response format:
{
  "status": [http status],
  "content": {
    "message": [message]
    }
}

500/Server Error response format:
{
  "status": [http status],
  "content": {
    "message": [message],
    "trace": [trace content]
    }
}

Open Issues:
============
Needs unit tests