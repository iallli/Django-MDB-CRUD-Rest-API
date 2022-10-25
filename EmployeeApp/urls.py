from django.urls import re_path as url
from EmployeeApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    url(r'^department$', views.departmentsApi),
    url(r'^department/([0-9]+)$', views.departmentsApi),

    url(r'^employee$', views.employeesApi),
    url(r'^employee/([0-9]+)$', views.employeesApi),

    url(r'^employee/savefile$', views.SaveFile)

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
