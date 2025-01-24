from . import models
from django.contrib import admin
#register the models
admin.site.register(models.Contact)
admin.site.register(models.Product)
admin.site.register(models.Orders)
admin.site.register(models.OrderUpdate)