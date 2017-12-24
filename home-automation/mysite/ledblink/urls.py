from django.conf.urls import url
from ledblink import views

urlpatterns=[
         url(r'^$', views.home, name='home'),
         #ur(r'^monitor/$',views.monitor,name='monitor'),
         #url(r'^control/$',views.control,name='control'),
         #url(r'^planth_health/$',views.planth_health,name='planth_health'),
        #url(r'^$',views.HomePageView, name='home'),
        #url(r'^$',views.led1,name='led1'),
        #url(r'^$',views.LedPageView.as_view(), name='led'),
         #url(r'^$',views.blinker),
         #url(r'^$',views.index, name='index'),
         #url(r'^led/$',views.led,name='led'),
         #url(r'^water_level/$',views.led,name='water_level'),
         #url(r'^temp/$',views.temp,name='temp'),
         #url(r'^buzzer/$',views.buz,name='buzzer'),
         #url(r'^pir/$',views.blinker,name='pir'),
         #url(r'^$',views.led,name='led'),
         #url(r'^$',views.led1),
        #url(r'^$',views.led,name='led'),
        #url(r'^admin/',views.blinker,name='index'),
]
