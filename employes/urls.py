from employes import views
from django.conf.urls import url 
from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView

urlpatterns = [

    url(r'^list/$', views.employes_list),
    url(r'^(?P<pk>\d+)/$', views.employes_detail),
    
    url(r'^salaire/list/$', views.salaires),
    url(r'^salaire/(?P<pk>\d+)/$', views.employes_salaire),

    url(r'^pointage/$', views.pointages),
    url(r'^pointage/(?P<pk>\d+)/$', views.employes_pointage),

    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),

]