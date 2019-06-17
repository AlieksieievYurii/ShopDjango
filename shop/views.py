from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
	goods = models.Goods.objects.order_by('?')
	title = 'Index'
	categories = models.Categories.objects.all()
	count_goods_in_cart = models.Cart.objects.all().count()
	content = {
		'goods': goods,
		'title': title,
		'categories': categories,
		'count_goods_in_cart': count_goods_in_cart
	}
	return render(request, 'shop/index.html', context=content)


def add_to_cart(request, goods_id: int):
	g = models.Goods.objects.get(id=goods_id)
	models.Cart.objects.Create(goods=g, count=1)
	return HttpResponseRedirect('/index/')


def remove_from_cart(request, goods_id: int):
	g = models.Goods.objects.get(id=goods_id)
	cart = models.Cart.objects(goods=q)
	cart.delete()
	return HttpResponseRedirect('/open_cart/')


def detail(request, goods_id: int):
	g = models.Goods.objects.get(id=goods_id)
	content = {
		'title': 'Detail',
		'product_name': g.name,
		'product_description': g.description,
		'product_count': g.available_count,
		'price': g.price,
		'img_url': g.img,
		'category': g.category.name
	}
	return render(request, 'shop/detail.html', context=content)


def open_cart(request):
	pass


def order(request):
	pass


def categories(request, categories_id: int):
	pass


def about(request):
	pass


def contact(request):
	pass