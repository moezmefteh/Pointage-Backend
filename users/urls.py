from users import views
from django.conf.urls import url 
from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView, EmployeDetail

urlpatterns = [

    url(r'^list/$', views.employes_list),
    path('<str:username>/', EmployeDetail.as_view()),
    
    url(r'^salaire/list/$', views.salaires),
    url(r'^salaire/(?P<pk>\d+)/$', views.employes_salaire),

    url(r'^pointage/list/$', views.pointages),
    url(r'^pointage/(?P<pk>\d+)/$', views.employes_pointage),

    url(r'^missions/list/$', views.missions),
    url(r'^missions/(?P<pk>\d+)/$', views.mission_detail),
    url(r'^mission/(?P<pk>\d+)/demarrer/$', views.demarrer_mission),
    url(r'^mission/(?P<pk>\d+)/terminer/$', views.terminer_mission),


    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),

]