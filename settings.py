import os
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')


ALLOWED_HOSTS = ['127.0.0.1'] # For Heroku deployment, you might want to specify your domain here
DEBUG = True # Set to False for Heroku deployment