from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^courses/$', views.index, name='index'),
    # ex: /polls/5/results/
    url(r'^add/$', views.add, name='add'),
    # ex: /polls/5/vote/
    url(r'^courses/(?P<course_id>[0-9]+)$', views.detail, name='detail'),
    url(r'^courses/(?P<course_id>[0-9]+)/change/$', views.change, name='change'),
]