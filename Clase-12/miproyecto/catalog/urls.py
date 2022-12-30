import django.conf.urls as url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index')
]

