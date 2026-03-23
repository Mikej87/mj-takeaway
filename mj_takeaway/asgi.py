import os
from django.core.asgi import get_asgi_application

# CRITICAL: This must match your project folder name followed by .settings
# Ensure there is a DOT between 'mj_takeaway' and 'settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mj_takeaway.settings')

application = get_asgi_application()