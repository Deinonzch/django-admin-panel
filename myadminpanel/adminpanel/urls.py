from django.urls import path
from . import views


app_name = 'adminpanel'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_model/', views.add_model, name='add_model'),
]