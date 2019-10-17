import falcon
from app.resource.product_list import ProductListResource
from app.resource.product_retrieve import ProductRetrieveResource
from app.data.products import ProductData

# pre-load products
ProductData.get_instance()

app = falcon.API()

app.add_route('/product', ProductListResource())
app.add_route('/product/{id}', ProductRetrieveResource())