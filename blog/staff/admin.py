from django.contrib import admin
from .models import Article, Publisher, Category

# Register your models here.
admin.site.register(Article)
admin.site.register(Publisher)
admin.site.register(Category)
