from django.shortcuts import render,redirect
from .models import Projects,ProjectAttendance
from .forms import ProjectForm,ProjectAttendanceForm

#projects
def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("projects:project_list")
    else:
        form = ProjectForm()
    return render(request,'projects/project_form.html',{'form':form})

def project_list(request):
    projects = Projects.objects.all()
    return render(request, "projects/project_list.html", {"projects": projects})
