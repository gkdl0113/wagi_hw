from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # 로그인/로그아웃
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='login.html'  # 직접 경로 지정
    ), name='login'),

]
