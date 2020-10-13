"""responsive_web URL Configuration

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
from django.urls import path
import portfolio.views
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portfolio.views.index, name='index'),
    path('about/', portfolio.views.about, name='about'),
    path('contact/', portfolio.views.contact, name='contact'),
    path('post/', portfolio.views.post, name='post'),
    path('post/<int:pk>/', portfolio.views.post_detail, name='post_detail'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('modal/', portfolio.views.modal, name='modal'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)