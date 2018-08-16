from django.urls import path

from .views import list_view, detail_view, add_view

urlpatterns = [
    path('', list_view, name='blog_index'),
    path('posts/<int:post_id>/', detail_view, name='blog_detail'),
    path('add', add_view, name='add_post')
]

