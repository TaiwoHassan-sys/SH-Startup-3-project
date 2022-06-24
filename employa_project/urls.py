from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path("", TemplateView.as_view(template_name ="index.htm"), name="index"),
    path('admin/', admin.site.urls),
    path('employee/',include('employee_register.urls')),
    path('auth/', include('djoser.urls')),
    path("docs/", include_docs_urls(title="Employees API")),
    path(
        "schema/",
        get_schema_view(
            title="Employee", description="API for the Employee", version="1.0.0"
        ),
        name="employee-schema",
    ),
]

