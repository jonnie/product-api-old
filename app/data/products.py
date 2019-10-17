import pandas as pd
import logging
from app.config import AppConfig

IN_STOCK_MAP = {
    'y'     : True,
    'yes'   : True,
    'true'  : True,
    'n'     : False,
    'no'    : False,    
    'false' : False,
}

logger = logging.getLogger(__name__)
logger_stream = logging.StreamHandler()
logger_stream.setLevel(logging.INFO)
logger.addHandler(logger_stream)
logger.setLevel(logging.INFO)

class ProductData:
    __instance = None
    __data = []

    @staticmethod
    def get_instance():
        if ProductData.__instance == None:
            logger.info('Loading products...')
            ProductData(ProductData._load_products())
            logger.info('Products successfully loaded')

        return ProductData.__instance

    def get_products(self):
        return ProductData.__data

    def __init__(self, data):
        if ProductData.__instance != None:
            raise Exception("Invalid use of class, call ProductData.get_instance() instead")
        else:
            ProductData.__instance = self
            ProductData.__data     = data

    def _import_products_from_csv(filename):
        products = pd.read_csv(filename, skipinitialspace=True)
        products = products.rename(columns={
            'Id'       : 'id',
            'Name'     : 'name',
            'Brand'    : 'brand',
            'Retailer' : 'retailer',
            'Price'    : 'price',
            'InStock'  : 'in_stock',
        })

        # Convert in_stock to either True or False
        products['in_stock'] = products['in_stock'].map(IN_STOCK_MAP)

        return products

    def _import_products_from_json(url):
        products = pd.read_json(url)

        # Convert in_stock to either True or False
        products['in_stock'] = products['in_stock'].map(IN_STOCK_MAP)

        return products    

    def _load_products():
        products_1 = ProductData._import_products_from_csv(AppConfig.PRODUCTS_CSV_FILEPATH)
        products_2 = ProductData._import_products_from_json(AppConfig.PRODUCTS_JSON_URL)

        # merge 2 products sets together
        products = pd.concat([products_1, products_2])

        # convert all prices to numeric and replace all non-numbers with NaN
        products['price'] = (
            pd.to_numeric(products['price'], errors='coerce')
        )

        # exclude free products (if EXCLUDE_FREE_PRODUCTS is True)
        if AppConfig.EXCLUDE_FREE_PRODUCTS:
            products = products[products['price'] > 0]

        # sort products by price ascending
        products = products.sort_values(by=['price'])

        # index products by 'id'
        products['idx'] = products['id']
        products = products.set_index('idx')
        products.index = products.index.map(str)

        return products