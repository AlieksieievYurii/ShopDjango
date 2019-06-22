from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def get_products(request, categories_id=None):
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
		'categories': models.Category.objects.all(),
		'count_goods_in_cart': models.Cart.objects.all().count()
	}

	return render(request, 'shop/index.html', context=content)


def index(request):
	return get_products(request)


def add_to_cart(request, goods_id: int):
	if request.method == 'POST':
		product = models.Product.objects.get(id=goods_id)
		try:
			product_from_car = models.Cart.objects.get(product=product)
			product_from_car.count += 1
			product_from_car.save()
		except ObjectDoesNotExist:
			models.Cart.objects.create(product=product, count=1)
	return HttpResponseRedirect('/index/')


def remove_from_cart(request, goods_id: int):
	if request.method == 'POST':
		product = models.Product.objects.get(id=goods_id)
		cart = models.Cart.objects.get(product=product)
		cart.delete()
	return HttpResponseRedirect('/cart/')


def detail(request, goods_id: int):
	content = {
		'title': 'Details',
		'product': models.Product.objects.get(id=goods_id),
		'categories': models.Category.objects.all(),
		'count_goods_in_cart': models.Cart.objects.all().count(),
		'category': models.Product.objects.get(id=goods_id).category.name
	}
	return render(request, 'shop/detail.html', context=content)


def cart(request):
	items_cart = []
	summa = 0
	for item in models.Cart.objects.all():
		summa_items = item.count * item.product.price
		summa += summa_items
		items_cart.append({
			'product': item,
			'price_for_all': summa_items
			})
	return render(request, 'shop/cart.html', context={
		'products': items_cart, 
		'summa': summa, 
		'categories': models.Category.objects.all(),
		'count_goods_in_cart': models.Cart.objects.all().count()})


def order(request):
	if request.method == 'POST':
		cart = models.Cart.objects.all().delete()
		return render(request, 'shop/order.html')
	else:
		raise Exception('Wrong request!')


def categories(request, categories_id: int):
	return get_products(request, categories_id)

def about(request):
	return render(request, 'shop/about.html', context={'count_goods_in_cart': models.Cart.objects.all().count()})


def contacts(request):
	return render(request, 'shop/contacts.html', context={'count_goods_in_cart': models.Cart.objects.all().count()})