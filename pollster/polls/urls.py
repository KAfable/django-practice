from django.urls import path

from . import views

# might need to create namespace, in case you have a `details` view in your polls app and shops app

app_name = 'polls'
urlpatterns = [path('', views.index, name='index')]
