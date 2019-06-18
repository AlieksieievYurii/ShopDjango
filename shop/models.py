from django.db import models

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name


class Product(models.Model):
	name = models.CharField(max_length=20)
	description = models.TextField()
	price = models.IntegerField()
	available_count = models.IntegerField()
	img = models.CharField(max_length=1000)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Cart(models.Model):
	product = models.OneToOneField(Product, on_delete=models.CASCADE)
	count = models.IntegerField()

	def __str__(self):
		return '{} -> {}'.format(self.product.name, self.count)

