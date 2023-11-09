from django.urls import path
from .views import * 
urlpatterns = [
    path('', home, name="home"),
    path('add-page/', add_user, name="add_user")
]
