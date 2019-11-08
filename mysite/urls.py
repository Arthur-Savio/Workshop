
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from ifalflix import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('ifalflix.urls'))
]  

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

