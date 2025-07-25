"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from .views import signup_view, home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # 👈 Homepage
    path('accounts/signup/', signup_view, name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('insights.urls')),
]

# touched on 2025-05-27T15:28:48.234368Z
# touched on 2025-07-09T21:54:11.529432Z
# touched on 2025-07-09T21:54:20.795977Z
# touched on 2025-07-09T21:54:35.087024Z
# touched on 2025-07-09T21:54:59.694829Z
# touched on 2025-07-09T21:55:21.739583Z
# touched on 2025-07-09T21:55:29.631121Z
# touched on 2025-07-09T21:56:00.206218Z
# touched on 2025-07-09T21:56:12.465496Z
# touched on 2025-07-09T21:56:19.011245Z
# touched on 2025-07-09T21:56:40.072490Z
# touched on 2025-07-09T21:56:44.595684Z
# touched on 2025-07-09T21:56:56.671200Z
# touched on 2025-07-09T21:57:10.441177Z
# touched on 2025-07-09T21:57:40.633835Z