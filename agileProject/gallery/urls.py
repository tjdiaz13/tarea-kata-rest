from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('addUser/', views.add_user_view, name='addUser'),
]
