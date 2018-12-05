from django.db import models

class Place(models.Model):
	placename = models.TextField()

	def __str__(self):
		return self.placename

class Publisher(models.Model):
	publishername = models.TextField()

	def as_dict(self):
		return {
			"name" : self.publishername
		}

	def __str__(self):
		return self.publishername

class Title(models.Model):
	titlename = models.TextField()

	def __str__(self):
		return self.titlename

class Category(models.Model):
	categoryname = models.TextField()

	def __str__(self):
		return self.categoryname

##on_delete=models.SET_NULL , null = True?

class Book(models.Model):
	name = models.TextField()
	author = models.CharField(max_length=200)
	publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE, null = True)
	title = models.ForeignKey(Title,on_delete=models.CASCADE, null = True)
	place = models.ForeignKey(Place,on_delete=models.CASCADE, null = True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null = True)
	pages = models.IntegerField()
	press = models.CharField(max_length=100)
	parts = models.IntegerField()
	notes = models.CharField(max_length = 100)




