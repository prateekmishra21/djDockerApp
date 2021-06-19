from django.contrib import admin
from django.urls import path
from app.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", Home)
]
