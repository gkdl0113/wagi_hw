# user/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import like_post, signup_view, write_post, post_list, post_detail, edit_post


urlpatterns = [
    # ✅ 로그인 / 로그아웃 / 회원가입
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='user/login.html'  # 우리가 만든 로그인 템플릿
    ), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/signup/', signup_view, name='signup'),

    # ✅ 게시글 관련 URL
    path('', post_list, name='post_list'),
    path('write/', write_post, name='write_post'),
    path('detail/<int:post_id>/', post_detail, name='post_detail'),
    path('edit/<int:post_id>/', edit_post, name='edit_post'),
    path('like/<int:post_id>/', like_post, name='like_post'),
    path('edit/<int:post_id>/', edit_post, name='edit_post'),
    path('detail/<int:post_id>/', post_detail, name='post_detail'),  # ← 이것도 꼭 있어야!

]

