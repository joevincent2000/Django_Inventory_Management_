from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Product,Location,ProductMovement)
class ViewAdmin(admin.ModelAdmin):
    pass