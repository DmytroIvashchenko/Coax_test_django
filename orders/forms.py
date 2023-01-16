from django import forms


class CustomerForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    profile_picture = forms.ImageField()


class OrderForm(forms.Form):
    user_name = forms.CharField(label='user_name', max_length=100)
    email = forms.EmailField(label='email', max_length=100)
    # product_name = forms.CharField(label='product_name', max_length=100)
    # price = forms.FloatField(label='price', max_value=200)
    # category = forms.CharField(label='category', max_length=20)
