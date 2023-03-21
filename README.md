# MOVIE-API-DJANGO

## Description
Todo app hecha con django-rest-framework y tiene las funciones de sign-up y login de usuarios y también creación de tareas.

## Run Locally

Clonar el repositorio

```bash
  https://github.com/Geffrerson7/TASK-API.git
```

Ir al directorio del proyecto

```bash
  cd API-TASK
```

## Setup
Crear un entorno virtual y lo activamos:

```sh
$ python virtualenv venv
# windows
$ source venv/Scripts/activate
# Linux
$ source venv/bin/activate
```

Luego instalar las librerias:

```sh
(env)$ pip install -r requirements.txt
```

Luego, realizamos las migraciones.
```sh
(env) $ python manage.py makemigrations
(env) $ python manage.py migrate
```

Una vez concluido, procedemos a iniciar la app
```sh
(env)$ python manage.py runserver
```

## Author
- [Gefferson Max Casasola Huamancusi](https://www.github.com/Geffrerson7)