from django.contrib import admin
from .models import categories, getpost
# Register your models here.

admin.site.register(getpost)
admin.site.register(categories)