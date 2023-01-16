import json
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from .forms import CustomerForm, OrderForm
from .models import Order, Customer, Category, Product


# залишилось з попереднього завдання функція створення користувача, url /order/create
def create_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            obj = Customer.objects.create(
                **form.cleaned_data
            )
            obj.save()
    else:
        form = CustomerForm()
    return render(request, 'orders/create.html', {'form': form})


# функція відображення товарів та категорій
def show(request):
    product = Product.objects.all()
    category = Category.objects.all()
    return render(request, 'orders/product.html', {'product': product, 'category': category})


# функція фільтрації по категоріям
# хотів зробити, щоб була миттєва фільтрація, зрозуміло що треба використовувати метод filter, але не вийшло
# тому зробив через нові url адреси, реалізовано тільки по вказаним категоріям
def filter_category(request, url):
    category = Category.objects.all()
    dict_of_category = {'Telephone': 1, 'Notebook': 2}
    if url in dict_of_category.keys():
        product_filter = Product.objects.filter(category_id=dict_of_category[url])
        return render(request, 'orders/product_filter.html', {'product': product_filter, 'category': category})


def show_order(request):
    orders = Order.objects.all()
    return render(request, 'orders/show_order.html', {'orders': orders})


# функція створення замовлення за ім'ям та електронною адресою,
# тому параметри категорія, вартість та назва продукту по дефолту встановив 0
def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            obj = Order.objects.create(
                **form.cleaned_data
            )
            obj.save()
    else:
        form = OrderForm()
    return render(request, 'orders/create.html', {'form': form})


# спроба зробити post запит через ajax, але коли заходиш за прикріпленим url то invalid request
# витратив день на вивчення цього, але не вдалось зробити, схоже що проблема в html/js файлах
def order_post(request):
    # request.is_ajax() is deprecated since django 3.1
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if is_ajax:
        if request.method == 'POST':
            data = json.load(request)
            order_get = data.get('payload')
            Order.objects.create(name=order_get['name'], email=order_get['email'])
            return JsonResponse({'status': 'Order added!'})
        return JsonResponse({'status': 'Invalid request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')
