from django.urls import path

from orders import views

urlpatterns = [
    path('customer/', views.create_customer, name='create_customer'),
    path('product/', views.show, name='product'),
    path('product/<slug:url>', views.filter_category, name='filter'),
    path('order/create', views.create_order, name='create_order'),
    path('order/', views.show_order, name='create_order'),
    path('order_post/', views.order_post, name='order_post'),

]
