from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^courses/$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^courses/(?P<course_id>[0-9]+)$', views.detail, name='detail'),
    url(r'^courses/(?P<course_id>[0-9]+)/change/$', views.change, name='change'),
]