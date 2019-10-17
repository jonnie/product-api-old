# Product API

## Setting up the environment
This guide assumes that Python 3 is already installed. To setup this project follow these instructions:

    make create_env activate_env install

Note: if you don't have `make` installed follow run this instead:

    python3 -m venv env
    . env/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt

Note: if you get an error stating `python3` cannot be found simply replace this with `python`

## Running the API app
This project uses gunicorn to launch the api, to run this command:

    make run

Or, if you don't have `make` installed, run this instead:

    gunicorn -b 127.0.0.1:8000 app.api:app

Hold down Ctrl+C to stop the server

## Access the API app
Use a tool like Postman to execute the following as examples:

List of products (limited to 50 by default): http://127.0.0.1:8000/product
List of products with specified limit: http://127.0.0.1:8000/product/?limit=100
Retrieve a single product by id: http://127.0.0.1:8000/product/8182756

## Configuration
Located at `app/config.py` is a class containing a series of configuration variables used by the app:

    EXCLUDE_FREE_PRODUCTS = True
    PRODUCTS_CSV_FILEPATH = 'data/products.csv.gz'
    PRODUCTS_JSON_URL     = 'https://s3-eu-west-1.amazonaws.com/pricesearcher-code-tests/python-software-developer/products.json'
    DEFAULT_PRODUCT_LIMIT = 50

These are the defaults and can be changed, however the server will need to be restarted for the changes to take effect.