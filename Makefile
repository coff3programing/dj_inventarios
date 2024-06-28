migrations:
	python manage.py makemigrations --settings=settings.local

migrate:
	python manage.py migrate --settings=settings.local

	
superuser:
	python manage.py createsuperuser --settings=settings.local


mrun: migrate
	python manage.py runserver --settings=settings.local

lrun:
	python manage.py runserver --settings=settings.local

prun:
	python manage.py runserver --settings=settings.prod
