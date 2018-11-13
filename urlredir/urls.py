from django.conf.urls import url
from django.contrib import admin

from redir import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^shorten/$', views.shorten, name='shorten'),
    url(r'^(?P<short_url>[\w-]+)/$', views.redirect_to_original, name='redirect_to_original'),
]
