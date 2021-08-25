
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^users/', include('users.urls')),

]
urlpatterns += staticfiles_urlpatterns()
