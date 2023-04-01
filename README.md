# TASK-API

## Description
All app made with django-rest-framework and has the functions of user sign-up and login and also task creation.

## Getting Started

First clone the repository from Github and switch to the new directory:
```bash
  $ clone git https://github.com/Geffrerson7/TASK-API.git
```

```bash
  $ cd TASK-API
```

Activate the virtualenv for your project.

```sh
$ virtualenv venv
# windows
$ source venv/Scripts/activate
# Linux
$ source venv/bin/activate
```

Install project dependencies:
```sh
(env)$ pip install -r requirements.txt
```

Then simply apply the migrations:
```sh
(env) $ python manage.py makemigrations
(env) $ python manage.py migrate
```

You can now run the development server:
```sh
(env)$ python manage.py runserver
```

And navigate to
```sh
http://127.0.0.1:8000/
```

## Author

- [Gefferson Max Casasola Huamancusi](https://www.github.com/Geffrerson7)
