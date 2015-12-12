from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')), #Django reindirizzerà ora tutto ciò che viene da 'http://127.0.0.1:8000/' verso blog.urls e cercherà ulteriori istruzioni in questo file.
]
