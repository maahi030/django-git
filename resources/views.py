from django.shortcuts import render,redirect
from .models import Resource,ResourceAttendace
from .forms import ResourceForm,ResourceAttendanceForm

def resource_create(request):
    if request.method == "POST":
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resources:resource_list')
    else:
        form = ResourceForm()
    return render(request,'resources/resource_form.html',{'form':form})

def resource_list(request):
    resources = Resource.objects.all()
    return render(request,'resources/resource_list.html',{'resources':resources})