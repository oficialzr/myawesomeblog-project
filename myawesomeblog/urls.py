from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import events.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', events.views.home, name='home'),
    path('posts/', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
