"""KidsMath URL Configuration

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
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from sitepanel.views import *
from math_exercises.views import *
from sitepanel.forms import ResetPasswordForm, PasswordResetConfirmForm

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('reset_password/', auth_views.PasswordResetView.as_view(
                            template_name='registration/password_reset_form.html',
                            form_class=ResetPasswordForm), name='reset_password'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
                            template_name='registration/password_reset_confirm.html',
                            form_class=PasswordResetConfirmForm), name='password_reset_confirm'),
    path('admin/', admin.site.urls),
    # path('test/', TestView.as_view(), name='test'),
    path('', IndexView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/', UserView.as_view(), name='user'),
    path('edit_profile/', EditProfileView.as_view(), name='edit_profile'),
    path('edit_profile/edit_password/', EditPasswordView.as_view(), name='edit_password'),
    path('verification/', include('verify_email.urls')),
    path('kids/', KidsView.as_view(), name='kids'),
    path('add_kids/', AddKidsView.as_view(), name='add_kids'),
]


urlpatterns += [
    path('category_choice/', CategoryView.as_view(), name='category'),
    path('play/(?P<category>[0-9]+)/(?P<amount>[0-9]+)/(?P<range_from>[0-9]+)/(?P<range_to>[0-9]+)/\\Z',
         PlayView.as_view(), name='play'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
