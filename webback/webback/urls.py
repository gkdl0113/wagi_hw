from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('post.urls')),
    #path('accounts/', include('django.contrib.auth.urls')),  # 로그인/로그아웃
    #path('accounts/login/', auth_views.LoginView.as_view(
    #    template_name='login.html'  # 직접 경로 지정
    #), name='login'),
    path('board/', include('user.urls')),

]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
