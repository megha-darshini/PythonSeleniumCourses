from woocommerce import API

wcapi = API(
    url="http://localhost:8888/demotestsite/",
    consumer_key="ck_7b2459a95446d9bf790732ddc5819ffa813cab52",
    consumer_secret="cs_744d98cf2902bdee6cbf16669c5ca629dc5d4dc7",
    version="wc/v3"
)

r = wcapi.get("products")

print(r.json())

import pprint
r = wcapi.get("orders")

pprint.pprint(r.json())
