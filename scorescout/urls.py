from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from .views import UserActivationView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    re_path(r'^activate/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$', UserActivationView.as_view()),
]
