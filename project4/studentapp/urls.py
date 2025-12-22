from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views  # <-- import home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('to_do_list.urls')),
    path('blog/', include('blog.urls')),
    path('notes/', include('upload_notes.urls')),
    path('', views.home, name='home'),  # <-- add this line
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
