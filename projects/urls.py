from django.urls import path
from . import views

app_name = "projects"

urlpatterns = [
    path("projectcreate/",views.project_create,name="project_create"),
    path("projectlist/",views.project_list,name="project_list")
]
