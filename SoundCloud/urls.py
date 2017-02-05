from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('accounts.urls', namespace="accounts")),
    url(r'^', include('SoundCloudApp.urls', namespace="SoundCloudApp")),
    url(r'^Elasticsearch/', include('haystack.urls')),
    url(r'^admin/', admin.site.urls),
]
