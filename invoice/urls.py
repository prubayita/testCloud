from django.urls import path
from . import views

app_name = 'invoice'

urlpatterns = [
    path('create-invoice/', views.create_invoice, name='create_invoice'),
    path('view-invoice/<int:receipt_id>/', views.view_invoice, name='view_invoice'),
]
