from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.main,name="hello"),
    path('about/',views.main1,name="hello"),
    path('service/',views.main2,name="hello"),
    path('contact/',views.main3,name="hello"),
]
