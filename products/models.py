from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)

class Photo(models.Model):
    product = models.ForeignKey(Product, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_photos/')
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('product', 'image', 'city')
