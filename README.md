# django-rest-react

Practice REST api w/ React frontend for final lambda school build week!

## Notes on Setup

1. start pipenv virtual environment.
2. add deps (django, djangorestframework, django-rest-knox).
3. create project with django-admin startproject <project name>.
4. ensure vscode interpreter is using pipenv version.
5. should now have a pipfile, pipfile.lock, and a folder with the project under the name given.
6. cd into the folder and generate a django app with:
   python manage.py startapp <name of app>
7. add the app to the settings.py in orig folder, as well as 'rest_framework'.
8. comes default with sqlite, but can change in the settings.py as well (info in django docs).
9. set up models for your 'app' in models.py file for specific app. (checkout leads folder for example)
10. run migrations for a specific 'app' with:
    python manage.py makemigrations <name of app>
11. add migrations to the db with:
    python manage.py migrate
12. this will also run all of the included django batteries-included migrations
13. set up serializer for model instance. serializers allow complex data types such as querysets and model instances to be converted to native python datatypes that can be easily rendered into JSON etc (we want our API to serve JSON).
14. see serializers.py for example.
15. create our API. A lot of what it generally takes to specify routes is abstracted away with viewsets. checkout api.py or the docs for examples.
16. setup include for main folder urls.py to point to apps urls.py.
17. setup router for apps urls.py as done in leads and you should have a basic rest api working.
18. run your server with python manage.py runserver
19. test that everythings working!
