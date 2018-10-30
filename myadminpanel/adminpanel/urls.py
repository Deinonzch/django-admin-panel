from django.urls import path
from . import views


app_name = 'adminpanel'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_model/', views.add_model, name='add_model'),
    path('<int:pk>/<str:app_name>/<str:model_name>/model/', views.ModelView.as_view(), name='view_model'),
]