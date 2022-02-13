from datetime import datetime
from django.db import models

# Create your models here.


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField(max_length=200)
    lot_size = models.DecimalField(max_digits=5)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo1 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True')
    photo2 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True')
    photo3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True')
    photo4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.title
    