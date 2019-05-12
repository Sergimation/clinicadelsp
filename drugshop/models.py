# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
from django.urls import reverse


class product(models.Model):
    reference = models.BigIntegerField(primary_key=True, default='')
    name = models.CharField(max_length=255, default="")
    price = models.FloatField(null=True)
    discount = models.FloatField(null=True, default=0)
    description = models.CharField(max_length=255, null=True)
    cart = models.ForeignKey(User, null=True, on_delete=models.CASCADE, default='')
    image = models.ImageField(upload_to='images/', default='images/None/no-img.jpg', null=True)
    register_time = models.DateTimeField(auto_now=True)
    buy = models.BooleanField(default=False)

    def averageRating(self):
        reviewCount = self.product_review_set.count()
        if not reviewCount:
            return 0
        else:
            ratingSum = sum([float(review.rating) for review in self.product_review_set.all()])
            return ratingSum / reviewCount

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('drugshop:product_detail', kwargs={'pk': self.pk})


class stock(models.Model):
    key = models.OneToOneField(product, on_delete=models.CASCADE,default="")
    quantitiy = models.IntegerField(null=True)

    def __str__(self):
        return self.key.name

    def available(self):
        if self.quantitiy >= 1:
            return True


class review(models.Model):
    ''' Review atributes '''
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    product = models.OneToOneField(product, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " " + self.product.name + " " + str(self.date)

