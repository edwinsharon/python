from django.contrib import admin
from .models import *


# Register your models here.
class Department_display(admin.ModelAdmin):
    list_display=['name']
class Position_display(admin.ModelAdmin):
    list_display=['height']
class Coach_display(admin.ModelAdmin):
    list_display=['name','position']        
class Player_display(admin.ModelAdmin):
    list_display=['name','coach','position']    
admin.site.register(Department,Department_display)
admin.site.register(Position,Position_display)
admin.site.register(Coach,Coach_display)
admin.site.register(Player,Player_display)