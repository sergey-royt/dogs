# migrations
make-migrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate