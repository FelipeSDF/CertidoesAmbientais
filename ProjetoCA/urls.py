"""
URL configuration for ProjetoCA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
# import reports.urls as reports_urls

from setup import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='home'),
    
    
    path('ReportFormPage/', views.ReportFormPage.as_view(), name='ReportFormPage'),
    # path('ReportPage/<pk>/', views.ReportPage.as_view(), name='ReportPage'),
    path('SaveRedirect', views.SaveReport.as_view(), name='SaveReport'),
    path('SaveReportFisicoRedirect', views.SaveReportFisico.as_view(), name='SaveReportFisico'),
    path('CertificatePage/', views.CertificatePage.as_view(), name='CertificatePage'),
    path('accounts/login/', views.LoginPage, name='LoginPage'),
    path('accounts/logout/', views.logut, name='logout'),
    path('CertificatePage/MakeCertificate', views.MakeCertificate.as_view(), name='MakeCertificate')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
