
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'blogpost/',include('blogpost.urls')),
    url(r'',include('blogpost.urls',namespace='blogpost',app_name='blogpost'))
   
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
