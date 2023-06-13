from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('sales-invoice/<int:pk>', views.sales_invoices, name='sales-invoices'),
    path('delete-invoice/<int:pk>', views.delete_invoice, name='delete-invoice'),
    path('update-invoice/<int:pk>', views.update_invoice, name='update-invoice'),
    path('add-invoice/', views.add_invoice, name='add-invoice'),
]
