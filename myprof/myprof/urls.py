"""myprof URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
# from django.contrib.staticfiles.storage import staticfiles_storage
# from django.views.generic.base import RedirectView
from django.conf import settings

admin.site.site_header = "My Portfolio"
admin.site.site_title = "My Portfolio Login"
admin.site.index_title = "My Portfolio Dashboard Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('main.urls')),
    path('about', include ('main.urls')),
    path('resume', include('main.urls')),
    path('projects', include ('main.urls')),
    # path('blog', include ('main.urls')),
    path('contact', include ('main.urls')),
    # path('contactsaveEnquiry', include ('main.urls')),
    # path('favicon.ico', RedirectView.as_view(url('static/img/favicon.ico')))
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
