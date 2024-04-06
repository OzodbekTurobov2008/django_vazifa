from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('myapp.urls')),
    path("about/",include('myapp.urls')),
    path("service/",include('myapp.urls')),
    path("contact/",include('myapp.urls')),
]
