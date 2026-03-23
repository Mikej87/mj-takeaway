import os
from django.core.wsgi import get_wsgi_application

# CRITICAL: This must match your project folder name followed by .settings
# If your folder is 'mj_takeaway', use 'mj_takeaway.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MJ_Takeaway.settings')

application = get_wsgi_application()