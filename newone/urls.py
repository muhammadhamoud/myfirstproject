"""newone URL Configuration

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
from django.contrib import admin
from django.urls import path

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views


import app.views
import app.forms

urlpatterns = [
    url(r'^$', app.views.home, name='home'),
    url(r'^about', app.views.about, name='about'),
    url(r'^contact',app.views.contact,name='contact'),
    url(r'^test', app.views.test, name='test'),
    # url(r'^login/$',
    #     django.contrib.auth.views.login,
    #     {
    #         'template_name': 'app/login.html',
    #         'authentication_form': app.forms.BootstrapAuthenticationForm,
    #         'extra_context':
    #         {
    #             'title': 'Log in',
    #             'year': datetime.now().year,
    #         }
    #     },
    #     name='login'),
    # url(r'^logout$',
    #     django.contrib.auth.views.logout,
    #     {
    #         'next_page': '/',
    #     },
    #     name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    path('admin/', admin.site.urls),
]
