web: gunicorn pip install wheel
web: gunicorn python setup.py bdist_wheel
web: gunicorn pip install flaskr-1.0.0-py3-none-any.whl
web: gunicorn export FLASK_APP=flaskr
web: gunicorn flask init-db
web: gunicorn --chdir ./flaskr __init__:app

