from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

app_info = (
    openapi.Info(
        title="Your API Title",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
)

schema_view = get_schema_view(
    app_info, public=True, permission_classes=(permissions.AllowAny)
)

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    # My apps
    path("api/auth/", include("users.urls"), name="auth"),
    path("api/boards/", include("boards.urls"), name="boards"),
    path("api/columns/", include("columns.urls"), name="columns"),
    path("api/tasks/", include("tasks.urls"), name="tasks"),
    path("api/subtasks/", include("subtasks.urls"), name="subtasks"),
    # Doc
    path(
        "swagger/",
        schema_view.with_ui(
            "swagger",
            cache_timeout=0,
        ),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
