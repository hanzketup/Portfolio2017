from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.list),
    url('^item', views.item),
]
