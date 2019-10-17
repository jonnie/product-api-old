class AppConfig:
    EXCLUDE_FREE_PRODUCTS = True
    PRODUCTS_CSV_FILEPATH = 'data/products.csv.gz'
    PRODUCTS_JSON_URL     = 'https://s3-eu-west-1.amazonaws.com/pricesearcher-code-tests/python-software-developer/products.json'
    DEFAULT_PRODUCT_LIMIT = 50