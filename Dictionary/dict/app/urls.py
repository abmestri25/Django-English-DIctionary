from django.urls import path
from .views import index
from app import views

urlpatterns = [
    path('index',views.index,name='index'),
]