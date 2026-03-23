import os
from pathlib import Path

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'fallback-key-for-local-only')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = ['your-app-name.herokuapp.com', '127.0.0.1']