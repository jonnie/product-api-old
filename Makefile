SHELL:=/bin/bash
NAME = product-api

create_env:
	@python3 -m venv env

activate_env:
	@. env/bin/activate

install:
	@pip install --upgrade pip
	@pip install -r requirements.txt

run:
	@gunicorn -b 127.0.0.1:8000 app.api:app