from django.contrib import admin
from .models import Stock, Toy
# Register your models here.

admin.site.register(Toy)
admin.site.register(Stock)