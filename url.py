from django.conf.rls.static import static
from django.contrib import admin
from django.urls import path, include

from . import settings 

urlpatterns = [
path('admin/', admin.site.urls),
path('', include('accounts.urls')),
path('', include('submission_portal.urls')),
path('', include('appointment_log.urls')),
path('', include('course_materials.urls')),
path('summernote/', include('django_summernote.urls')),
]= static(settings.MEDIA_URL, document_root = 'settings_MEDIA_ROOT')