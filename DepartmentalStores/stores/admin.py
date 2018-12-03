from django.contrib import admin
from .models import Location, Department, Category, SubCategory

admin.site.register(Location)
admin.site.register(Department)
admin.site.register(Category)
admin.site.register(SubCategory)
