# user/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import like_post, write_post, post_list, post_detail, edit_post


urlpatterns = [
   
    # ✅ 게시글 관련 URL
    path('home/', post_list, name='post_list'),
    path('write/', write_post, name='write_post'),
    path('detail/<int:post_id>/', post_detail, name='post_detail'),
    path('edit/<int:post_id>/', edit_post, name='edit_post'),
    path('like/<int:post_id>/', like_post, name='like_post'),
    path('edit/<int:post_id>/', edit_post, name='edit_post'),
    path('detail/<int:post_id>/', post_detail, name='post_detail'),  # ← 이것도 꼭 있어야!
    
]

