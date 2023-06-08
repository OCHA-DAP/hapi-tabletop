from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("update/", views.update, name="update"),
    path("api/indicators/<str:indicatorName>", views.api, name="api"),
    path(
        "transform/<str:indicatorName>", views.transformload, name="transform"
    ),
]
