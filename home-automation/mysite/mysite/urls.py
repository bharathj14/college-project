"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
#from ledblink import views
from django.contrib import admin
from django.contrib.auth import views
from ledblink.forms import LoginForm

'''
urlpatterns=patterns('',
	url(r'^ledblink/$',blinker),
	)
'''
urlpatterns = [
    #url(r'^',include('ledblink.views')),
   # url(r'^$',views.index, name='index'),
    #url(r'^',include('ledblink.urls',namespace='ledblink')),
    #url(r'^admin/', admin.site.urls),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('ledblink.urls',namespace='ledblink')),
    url(r'^login/$', views.login, {'template_name': 'blog/login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/login'}), 
    ]

