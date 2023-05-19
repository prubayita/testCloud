from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name='app'),
    path('details/<int:id>', views.details, name='details'),
]