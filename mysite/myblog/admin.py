from django.contrib import admin
from myblog.models import Category, Post

admin.site.register(Post)
admin.site.register(Category)

#class CategoryInline(admin.TabularInline):
 #   model = Category.posts.through

#@admin.register(Post)
#class Post #fill me in
 #   inline =


#@admin.register(Category)
#class CategoryAdmin(admin.ModelAdmin)
 #   exclude = ['posts']
