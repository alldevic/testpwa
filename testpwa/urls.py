from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from .views import home, send_push

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('send_push', send_push),
    path('webpush/', include('webpush.urls')),
    path('sw.js', TemplateView.as_view(template_name='sw.js',
                                       content_type='application/x-javascript'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
