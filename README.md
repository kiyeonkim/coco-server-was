# [COCO Project](https://github.com/NA5G/coco-server-was)

## Table of contents

* [Quick start](#quick-start)
* [Documentation](#documentation)
* [Copyright and license](#copyright-and-license)

## Quick start

### Requirements
* [Python (2.7.x)](https://www.python.org/downloads/release/python-279/)
* [Postgres.app](http://postgresapp.com/)

### OS X
* Clone the repo:
```bash
> git clone https://github.com/NA5G/coco-server-was.git
> cd coco-server-was
```

* Make sure you have `pip` and `virtualenv` installed:
```bash
> brew install pip
> pip install virtualenv
```

* Install the necessary packages:
```bash
> source env/bin/activate
(env)> pip install -r requirements.txt
(env)> pip install -r requirements-test.txt
```
If you want deactivate the virtualenv, use:
```bash
(env)> deactivate
```
* Move to the coco project directory:
```bash
(env)> cd coco
```

* Copy coco/local_settings.py.default to coco/local_settings.py and edit to match your current environment.
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '[YOUR_DATABASE_NAME]',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

* Run the server:
```bash
(env)> python ./manage.py runserver
```

* **If you install/uninstall python packages, you have to update the requirements.txt**
```bash
(env)> pip freeze > requirements.txt
```

## Documentation

* [Meeting minutes](https://github.com/NA5G/coco-doc-meeting-minutes)


## Copyright and license

Code and documentation copyright 2015 Team NA5G. Code released under [the MIT license](https://github.com/twbs/bootstrap/blob/master/LICENSE).

