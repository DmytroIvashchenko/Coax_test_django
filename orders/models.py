from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    profile_picture = models.ImageField(upload_to='static/profile_pictures')

    def __str__(self):
        return f'{self.name}'


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='category')
    user = models.ForeignKey(to=Customer, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return f'User: {self.user} product: {self.name} category: {self.category}'


class Order(models.Model):
    user_name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100)
    product_name = models.TextField(max_length=100, default='None')
    price = models.IntegerField(default=0)
    category = models.TextField(max_length=100, default='None')

    def __str__(self):
        return f'{self.user_name} - {self.email} {self.product_name}, {self.price}, {self.category}'
