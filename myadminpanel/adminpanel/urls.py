from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('int:myadminpanel_id/', views.add_model, name='add_model'),
]
