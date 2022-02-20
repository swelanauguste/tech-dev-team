from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from core import views

urlpatterns = [
    # path("", TemplateView.as_view(template_name="index.html"), name="home"),
    path("", views.DocumentListView.as_view(), name="list"),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    # path("search/", views.SearchListView.as_view(), name="search"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
