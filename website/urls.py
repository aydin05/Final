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
    path('add-customer/', views.add_customer, name='add-customer'),
    path('add-article/', views.add_article, name='add-article'),
    path('articles/', views.articles, name='articles'),
    path('article/<int:pk>', views.article, name='article'),
    path('update-article/<int:pk>', views.update_article, name='update-article'),
    path('update-customer/<int:pk>', views.update_customer, name='update-customer'),
    path('customers/', views.customers, name='customers'),
    path('customer/<int:pk>', views.customer, name='customer'),
    path('delete-customer/<int:pk>', views.delete_customer, name='delete-customer'),
]
