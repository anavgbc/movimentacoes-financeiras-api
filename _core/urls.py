from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include("cnabfile.urls")),
    path('api/', include("stores.urls"))
]
