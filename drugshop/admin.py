# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from drugshop.models import product, stock, review

admin.site.register(product)
admin.site.register(stock)
admin.site.register(review)

