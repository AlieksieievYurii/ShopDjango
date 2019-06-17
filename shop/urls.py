from django.urls import path
from . import views

urlpatterns = [
	path('index/', views.index),
	path('add_to_cart/<int: goods_id>/', views.add_to_cart),
	path('remove_from_cart/<int: goods_id>/', views.remove_from_cart),
	path('goods/detail/<int: goods_id>/',views.detail),
	path('open_cart/<int: goods_id>/', views.open_cart),
	path('order/', views.order),
	path('categories/<int: categories_id>/', views.categories),
	path('about/', views.about),
	path('contact/', views.contact)
]