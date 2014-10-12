#/bin/bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver --settings=sdh.local_settings

