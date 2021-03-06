from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.inventory_list, name='inventory_list'),
    url(r'^inventory/(?P<pk>\d+)/$', views.inventory_detail, name='inventory_detail'),
    url(r'^inventory/new/$', views.inventory_new, name='inventory_new'),
    url(r'^inventory/(?P<pk>\d+)/edit/$', views.inventory_edit, name='inventory_edit'),
]
