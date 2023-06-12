from django.contrib import admin
from .models import Article, SalesInvoice, Customer

admin.site.register(Article)
admin.site.register(SalesInvoice)
admin.site.register(Customer)