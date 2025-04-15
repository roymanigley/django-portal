from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls
from django.views.generic import TemplateView

handler404 = "apps.shared.views.page_not_found_view"
handler403 = "apps.shared.views.page_permission_denied_view"
handler500 = "apps.shared.views.page_unexpected_error_view"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.authentication.urls')),
    path('', include('apps.portal.urls')),
    path('403/', TemplateView.as_view(template_name='errors/403.html'), name='403'),
    path('404/', TemplateView.as_view(template_name='errors/404.html'), name='404'),
    path('500/', TemplateView.as_view(template_name='errors/500.html'), name='500'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += debug_toolbar_urls()
