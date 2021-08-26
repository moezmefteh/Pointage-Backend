from users import views
from django.conf.urls import url 
from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView, EmployeDetail

urlpatterns = [

    url(r'^list/$', views.employes_list),
    url(r'(?P<username>\w{0,50})/$', views.EmployeDetail),
    
    url(r'^salaire/list/$', views.salaires),
    url(r'^salaire/(?P<user>\w{0,50})/$', views.employes_salaire),

    url(r'^pointage/list/$', views.pointages),
    url(r'^pointage/(?P<user>\w{0,50})/$', views.employes_pointage),

    url(r'^missions/list/$', views.missions),
    url(r'missions/(?P<user>\w{0,50})/$', views.mission_detail),
    url(r'^mission/(?P<pk>\d+)/demarrer/$', views.demarrer_mission),
    url(r'^mission/(?P<pk>\d+)/terminer/$', views.terminer_mission),


    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),

]