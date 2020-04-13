# Django API with JWT Authentication

DRF with JWT token validation.

Requirements to run this project. Python 3

Clone the repo to your computer. For example, to place it on your Desktop. cd ~/Desktop git clone https://github.com/Pragesh-yadav/drf-api-with-jwt.git 
cd drf-api-with-jwt

 set up our virtual environment 
  I’m going to use pipenv here—make sure you have it installed, then navigate to the directory you want your project to be in and run:
    **pipenv install**
Activate the virtual environment with
**pipenv shell**
Now install some packages, including Django, Django REST framework (hereafter referred to as the DRF), Django REST framework JWT, and Django CORS headers
**pipenv install django
pipenv install djangorestframework
pipenv install djangorestframework-jwt
pipenv install django-cors-headers**

we need to create a user, and before do that, we need to apply our migrations. Run the following:
**python manage.py migrate**
Create a new user is with:
  **python manage.py createsuperuser**
  Now start development server
  
  **python manage.py runserver**
  
  To get the JWT token navigate to
  **http://localhost:8000/token-jwt-auth/**
  
  Now api can be utilised to get the create,get , update and delete book records.

