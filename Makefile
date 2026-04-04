lint: ruff

ruff:
	ruff format
	ruff check --fix

data:
	python manage.py migrate
	python -Xutf8 manage.py loaddata mysite_data.json

run:
	python manage.py runserver

dumpdata:
	python -Xutf8 manage.py dumpdata --indent=2 --output=mysite_data.json

migrate:
	python manage.py makemigrations
	python manage.py migrate

schema:
	python manage.py spectacular --file schema.yml

db_flush:
	python manage.py flush

shell_plus:
	python manage.py shell_plus --print-sql
