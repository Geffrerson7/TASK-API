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

Create the virtual enviroment
```bash
  $ virtualenv venv
```

Activate the virtual enviroment for your project.
```bash
# windows
$ source venv/Scripts/activate
# Linux
$ source venv/bin/activate
```

Install project dependencies:
```sh
(venv)$ pip install -r requirements.txt
```

Then simply apply the migrations:
```sh
(venv) $ python manage.py makemigrations
(venv) $ python manage.py migrate
```

You can now run the development server:
```sh
(venv)$ python manage.py runserver
```

And navigate to
```sh
http://127.0.0.1:8000/
```

## Local Installation with Docker

Clone the respository

```bash
$ git clone https://github.com/Geffrerson7/TASK-API.git
```

Navigate to the new directory

```bash
$ cd TASK-API
```

Run the command
```sh
$ docker-compose up
```

And navigate to
```sh
http://127.0.0.1:8000/
```

## Author

- [Gefferson Max Casasola Huamancusi](https://www.github.com/Geffrerson7)
