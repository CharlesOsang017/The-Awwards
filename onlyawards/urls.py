from django.conf.urls import url,include
from django.contrib import admin
import awards

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('awards.links')),
    
]
