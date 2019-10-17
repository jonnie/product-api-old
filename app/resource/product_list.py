import falcon
from app.data.products import ProductData
from app.config import AppConfig
import json

class ProductListResource:

    def on_get(self, req, resp):

        limit = req.get_param('limit', required=False, default=str(AppConfig.DEFAULT_PRODUCT_LIMIT))

        self._validate(limit)

        products = ProductData.get_instance().get_products()        

        resp.status = falcon.HTTP_200        
        resp.media = json.loads(products.head(n=int(limit)).to_json(orient='records'))

    def _validate(self, limit):
        if not limit.isnumeric():
            raise falcon.HTTPBadRequest('limit parameter should be numeric')