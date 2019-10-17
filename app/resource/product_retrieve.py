import falcon
from app.data.products import ProductData
import json

class ProductRetrieveResource:
    def on_get(self, req, resp, id):

        try:
            product = ProductData.get_instance().get_products().loc[id]
        except KeyError:
            raise falcon.HTTPNotFound(description='Product with id {id} was not found'.format(id=id§))

        resp.status = falcon.HTTP_200
        resp.media = json.loads(product.to_json())