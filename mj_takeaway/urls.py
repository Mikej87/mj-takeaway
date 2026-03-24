from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # The backend you just set up
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('tracker.urls')),  # Points to your app's specific URLs
]