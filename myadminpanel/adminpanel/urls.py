from django.urls import path
from . import views


app_name = 'adminpanel'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_model/', views.add_model, name='add_model'),
    path('<int:pk>/<str:app_name>/<str:model_name>/model/', views.ModelView.as_view(), name='view_model'),
    path('<int:pk>/<str:app_name>/<str:model_name>/model/create/',
         views.CreateObjectView.as_view(success_url="/adminpanel/"),
         name='createview_model'),
    path('<int:pk>/<str:app_name>/<str:model_name>/<int:object_id>/model/update/',
         views.UpdateObjectView.as_view(success_url="/adminpanel/"),
         name='updateview_model'),
    path('<int:pk>/<str:app_name>/<str:model_name>/<int:object_id>/model/delete/',
         views.DeleteObjectView.as_view(success_url="/adminpanel/"),
         name='deleteview_model'),
]