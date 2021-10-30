from django.db import models


# Category Model
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name


# Products Model
class Products(models.Model):
    category = models.ForeignKey('Category', related_name='product', null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title
