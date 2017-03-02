from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^courses/$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^courses/(?P<course_id>[0-9]+)$', views.detail, name='detail'),
    url(r'^courses/(?P<course_id>[0-9]+)/change/$', views.change, name='change'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)