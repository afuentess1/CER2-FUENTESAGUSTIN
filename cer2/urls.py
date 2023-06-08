from django.contrib import admin
from django.urls import path
from comunicados import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

admin.site.login = login_required(admin.site.login)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.comunicados_filter, name='comunicados_filter'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
