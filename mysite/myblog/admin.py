from django.contrib import admin
from myblog.models import Category, Post

admin.site.register(Post)
admin.site.register(Category)
