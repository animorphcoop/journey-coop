from django.contrib import admin
from django.urls import path, include
from django.conf import settings


# https://docs.djangoproject.com/en/4.2/topics/http/views/#customizing-error-views
handler404 = 'main.views.error_handler'
handler500 = 'main.views.error_handler'
handler403 = 'main.views.error_handler'
handler400 = 'main.views.error_handler'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'))
]

if settings.DEBUG:
    import debug_toolbar

    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
        path("__reload__/", include('django_browser_reload.urls')),

    ] + urlpatterns



