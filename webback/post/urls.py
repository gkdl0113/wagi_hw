# user/urls.py

from django.urls import path
from .views import login_view, signup_view, logout_view
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', login_view, name='login'),  # 로그인 페이지
    #path('home/', post_list, name='post_list'),  # 로그인 성공 시 이동
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('accounts/signup/', signup_view, name='signup'),
    #path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    #logout_view,

]
