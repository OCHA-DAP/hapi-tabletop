from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("update/", views.update, name="update"),
    path("api/indicators/<str:indicator_name>", views.api, name="api"),
    path(
        "transform/<str:indicator_name>", views.transformload, name="transform"
    ),
]
