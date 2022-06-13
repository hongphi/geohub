from django.db import models
from autoslug.fields import AutoSlugField


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name', max_length=120, editable=False, always_update=True)
    price = models.FloatField()
    description = models.TextField(blank=True)
    os = models.CharField(max_length=100)


class ActivityLog(models.Model):
    path = models.CharField(max_length=500)
    meta_data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class Order(models.Model):
    STATUS_CHOICE = (
        ('new', "New"),
        ('paid', "Paid"),
        ('canceled', "Canceled"),
    )
    total = models.FloatField()
    status = models.CharField(max_length=20, default='new', choices=STATUS_CHOICE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
