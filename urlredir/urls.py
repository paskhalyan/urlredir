from django.conf.urls import url
from django.contrib import admin

from redir import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^shorten/', views.shorten, name='shorten'),
]
