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


def add_to_cart(request):
	pass


def remove_from_cart(request):
	pass


def detail(request):
	pass


def open_cart(request):
	pass


def order(request):
	pass


def categories(request):
	pass


def about(request):
	pass


def contact(request):
	pass