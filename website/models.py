from django.db import models


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_length=10, decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name


class SalesInvoice(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ('cash', 'Cash'),
        ('credit_card', 'Credit Card'),
        ('bank_transfer', 'Bank Transfer'),
    )

    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    articles = models.ManyToManyField(Article)
    invoice_date = models.DateField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_length=10, decimal_places=2, max_digits=10)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)

    def __str__(self):
        return f"Invoice #{self.pk}"
