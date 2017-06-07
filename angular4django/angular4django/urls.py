from django.conf.urls import url, include

from django.conf import settings
from django.contrib.staticfiles import views
from django.conf.urls.static import static
from angular4django.api import urls


urlpatterns = [
    url(r'^api/', include('angular4django.api.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 

