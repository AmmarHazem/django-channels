from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^(?P<room_name>[^/]+)/$', views.Room.as_view(), name='room'),
]