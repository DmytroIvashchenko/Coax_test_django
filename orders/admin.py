from django.contrib import admin

from orders.models import Customer, Order, Product, Category


class Product_admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'user')
    search_fields = ('price',)
    list_filter = ('category',)


class Category_admin(admin.ModelAdmin):
    list_display = ('id', 'name')


class Order_admin(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'product_name', 'category', 'price')


class Customer_admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'profile_picture')


admin.site.register(Category, Category_admin)
admin.site.register(Product, Product_admin)
admin.site.register(Order, Order_admin)
admin.site.register(Customer, Customer_admin)
