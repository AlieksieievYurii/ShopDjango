from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def get_products(request, categories_id: int = None, key_words: str = None):
	products = None
	category = None
	if categories_id is not None:
		category = models.Category.objects.get(id=categories_id)
		products = models.Product.objects.filter(category=category)
	else:
		products = models.Product.objects.order_by('?')

	if key_words:
		products = products.filter(Q(name__contains=key_words) | 
			Q(description__contains=key_words))

	_products = []
	for p in products:
		pr = {'product': p}
		_p = models.Cart.objects.filter(product=p).first()
		if _p:
			pr['is_in_cart'] = True
			pr['count'] = _p.count
		else:
			pr['is_in_cart'] = False
		_products.append(pr)
	content = {
		'products': _products,
		'title': category.name if category else 'Shop',
		'category': category.name if category else None,
		'categories': models.Category.objects.all(),
		'count_goods_in_cart': models.Cart.objects.all().count()
	}

	return render(request, 'shop/index.html', context=content)


def index(request):
	return get_products(request, key_words=request.GET.get('key_words', None))


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
	p = models.Product.objects.get(id=goods_id)
	content = {
		'title': 'Details',
		'product': p,
		'categories': models.Category.objects.all(),
		'count_goods_in_cart': models.Cart.objects.all().count(),
		'category': models.Product.objects.get(id=goods_id).category.name
	}

	_p = models.Cart.objects.filter(product=p).first()
	if _p:
		content['is_in_cart'] = True
		content['count_in_cart'] = _p.count
	else:
		content['is_in_cart'] = False
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
	content={
	'count_goods_in_cart': models.Cart.objects.all().count(),
	'categories': models.Category.objects.all()
	}
	return render(request, 'shop/about.html', context=content)


def contacts(request):
	content={
	'count_goods_in_cart': models.Cart.objects.all().count(),
	'categories': models.Category.objects.all()
	}
	return render(request, 'shop/contacts.html', context=content)