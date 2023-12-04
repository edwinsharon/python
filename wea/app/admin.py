from django.contrib import admin

# Register your models here.
from . models import *


class Image_display(admin.ModelAdmin):
    list_display=['img']


admin.site.register(Destination,Image_display)