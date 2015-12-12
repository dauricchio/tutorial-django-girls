from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    #assegnando una view nominata post_list alla URL ^$
    #il nome dell'URL che verrà usata per identificare la view.
]