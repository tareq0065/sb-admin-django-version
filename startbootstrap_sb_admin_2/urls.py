"""startbootstrap_sb_admin_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from django.conf.urls import url


from .views import (
    home_page_detail,
    blank_page,
    buttons_page,
    flot_page,
    forms_page,
    grid_page,
    icons_page,
    login_page,
    morris_page,
    notifications_page,
    panel_page,
    tables_page,
    typography_page
) 


urlpatterns = [
    url(r'^$', home_page_detail, name='home'),
    url(r'^blank/$', blank_page, name='blank'),
    url(r'^buttons/$', buttons_page, name='buttons'),
    url(r'^flot/$', flot_page, name='flot'),
    url(r'^forms/$', forms_page, name='forms'),
    url(r'^grid/$', grid_page, name='grid'),
    url(r'^icons/$', icons_page, name='icons'),
    url(r'^login/$', login_page, name='login'),
    url(r'^morris/$',morris_page, name='morris'),
    url(r'^notifications/$', notifications_page, name='notifications'),
    url(r'^panel/$', panel_page, name='panel'),
    url(r'^tables/$', tables_page, name='tables'),
    url(r'^typography/$', typography_page, name='typography'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
