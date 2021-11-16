"""CovidProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from Covid_Module.views import index
from django.conf.urls.static import static
from django.conf import settings

from Registration_Module import views as registerViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Covid_Module.urls')),
    path('social/',include('Social_Module.urls')),
    path('resources/', include('Resources_Module.urls')),

    path('register/', registerViews.index, name='registration-index'),
    path('register/user/', registerViews.register_user, name='registration-register'),
    path('register/hospital/staff/', registerViews.register_hospital_staff, name='registration-hospital-user'),
    path('login/', registerViews.login_request, name='registration-login'),
    path('logout/', registerViews.signout, name='registration-signout'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
