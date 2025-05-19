# user/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import custom_login, like_post, signup_view, write_post, post_list, post_detail, edit_post, logout_view


urlpatterns = [
    path('', custom_login, name='login'),  # 로그인 페이지
    path('home/', post_list, name='post_list'),  # 로그인 성공 시 이동
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/signup/', signup_view, name='signup'),

    # ✅ 게시글 관련 URL
    path('home/', post_list, name='post_list'),
    path('write/', write_post, name='write_post'),
    path('detail/<int:post_id>/', post_detail, name='post_detail'),
    path('edit/<int:post_id>/', edit_post, name='edit_post'),
    path('like/<int:post_id>/', like_post, name='like_post'),
    path('edit/<int:post_id>/', edit_post, name='edit_post'),
    path('detail/<int:post_id>/', post_detail, name='post_detail'),  # ← 이것도 꼭 있어야!
    path('login/', custom_login, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
]

