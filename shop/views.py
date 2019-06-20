from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
# Create your views here.

def get_products(request, categories_id=None):
	categories = models.Category.objects.all()
	count_goods_in_cart = models.Cart.objects.all().count()
	products = None
	category = None
	if categories_id is not None:
		category = models.Category.objects.get(id=categories_id)
		products = models.Product.objects.filter(category=category)
	else:
		products = models.Product.objects.order_by('?')
	content = {
		'goods': products,
		'title': category.name if category else 'Shop',
		'category': category.name if category else None,
		'categories': categories,
		'count_goods_in_cart': count_goods_in_cart
	}

	return render(request, 'shop/index.html', context=content)


def index(request):
	return get_products(request)


def add_to_cart(request, goods_id: int):
	if request.method == 'POST':
		product = models.Product.objects.get(id=goods_id)
		product_from_car = models.Cart.objects.filter(product=product)
		if product_from_car.count():
			product_from_car.count = product_from_car.count + 1
			product_from_car.save() 
		else:
			models.Cart.objects.create(product=product, count=1)
	return HttpResponseRedirect('/index/')


def remove_from_cart(request, goods_id: int):
	g = models.Product.objects.get(id=goods_id)

	cart = models.Cart.objects.get(goods=g)
	cart.delete()
	return HttpResponseRedirect('/open_cart/')


def detail(request, goods_id: int):
	product = models.Product.objects.get(id=goods_id)
	content = {
		'title': 'Details',
		'product': product
	}
	return render(request, 'shop/detail.html', context=content)


def cart(request):
	return render(request, 'shop/cart.html', context=None)


def order(request):
	pass


def categories(request, categories_id: int):
	return get_products(request, categories_id)

def about(request):
	return render(request, 'shop/about.html', context=None)


def contacts(request):
	return render(request, 'shop/contacts.html', context=None)