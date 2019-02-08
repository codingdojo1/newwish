from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name="index"),
  url(r'^new/$', views.new, name="new"),
  url(r'^create/$', views.create, name="create"),
  url(r'^delete/$', views.delete, name="delete"),
  url(r'^grant/$', views.grant, name="grant"),
#   url(r'^show/(?P<wish_id>\d+)/$', views.show, name="show"),
  url(r'^edit/(?P<wish_id>\d+)/$', views.edit, name="edit"),
#   url(r'^update/(?P<wish_id>\d+)/$', views.update, name="update"),
#   url(r'^delete/(?P<wish_id>\d+)/$', views.delete, name="delete"),
]
