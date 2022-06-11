"""sclWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views, settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

handler404 = 'sclWebsite.views.handler404'
handler500 = 'sclWebsite.views.handler500'
handler400 = 'sclWebsite.views.handler400'
handler403 = 'sclWebsite.views.handler403'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('testimonials/', views.about, name='about'),
    path('logout/', views.my_logout, name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='authorization/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='authorization/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='authorization/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='authorization/password_reset_complete.html'),
         name='password_reset_complete'),
    path('', views.index, name='home'),
    path('user/', include('users.urls')),
    path('teams/', include('teams.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
