from chef_chantier import views
from django.conf.urls import url 

urlpatterns = [

    url(r'^missions/$', views.missions),
    url(r'^missions/(?P<pk>\d+)/$', views.mission_detail),
    url(r'^mission/(?P<pk>\d+)/demarrer/$', views.demarrer_mission),
    url(r'^mission/(?P<pk>\d+)/terminer/$', views.terminer_mission),


]