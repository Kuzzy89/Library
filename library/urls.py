
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("library.accounts.urls")),
    path("accounts/", include("library.author.urls")),
    path("pets/", include("library.book.urls")),
    path("photos/", include("library.common.urls")),
]
