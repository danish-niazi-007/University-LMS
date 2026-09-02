from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path(
        "admin/",
        admin.site.urls,
    ),

    path(
        "",
        include("apps.accounts.urls"),
    ),

    path(
        "",
        include("apps.lms_assignments.urls"),
    ),
    path("", include("apps.attendance.urls")),
    path("", include("apps.assessments.urls")),path("", include("apps.courses.urls")),
    path("", include("apps.enrollments.urls")),
    path("", include("apps.hod.urls")),

]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )