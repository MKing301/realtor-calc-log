from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('commission/', include('commission.urls')),
    path('admin/', admin.site.urls),
]
