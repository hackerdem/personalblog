from django.conf.urls import url,include
from . import views


urlpatterns=[
    #url(r'blogpost',views.blogpost,name='blogpost'),
    url(r'contact',views.contact,name='contact'),
    url(r'search_results',views.search_results,name='search_results'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
    url(r'^$',views.index,name='index'),
    
]