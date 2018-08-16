from django.contrib import admin
from myblog.models import Category, Post


class CategoryInline(admin.TabularInline):
    model = Category.posts.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ['posts']
