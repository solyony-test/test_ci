env:
	virtualenv env

requirments:
	env/bin/pip install -r requirements.txt

test:
	env/bin/python manage.py test
