"""aaaimxemail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls import include, url

# static files imports
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Django REST Frammework
# https://www.django-rest-framework.org

from rest_framework import routers
from emails.views import EmailViewSet, TemplateViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"emails", EmailViewSet)
router.register(r"templates", TemplateViewSet)

# Admin Site 
admin.site.site_header = "AAAIMX Email Admin"
admin.site.site_title = "AAAIMX Email Admin"
admin.site.index_title = "Welcome to AAAIMX Email Administration"
admin.site.site_url = "/api"

urlpatterns = [
    path('', admin.site.urls),
    url(r"^api/", include(router.urls)),
]

# Static files urls development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
