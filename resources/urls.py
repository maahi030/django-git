from django.urls import path
from . import views

app_name = "resources"

urlpatterns = [
    path("resourcecreate/",views.resource_create,name="resource_create"),
    path("resourcelist/",views.resource_list,name="resource_list")
]
