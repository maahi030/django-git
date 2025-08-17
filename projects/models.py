from django.db import models
from resources.models import Resource

class Projects(models.Model):
    PROJECT_TYPE_CHOICES = [
        ('REGULAR', 'Regular Project'),
        ('FIXED_COST', 'Fixed Cost Project'),
    ] 
    project_name = models.CharField(max_length=100,help_text="Name of the project")
    project_type = models.CharField(max_length=20,choices=PROJECT_TYPE_CHOICES,default='REGULAR')
    start_year = models.PositiveIntegerField(help_text="Year when the project started")
    end_year = models.PositiveIntegerField(null=True,blank=True,help_text="Year when the project ended")
    start_month = models.PositiveIntegerField(help_text="Month when the project started")
    end_month = models.PositiveIntegerField(null=True,blank=True,help_text="Month when the project ended")
    is_active = models.BooleanField(default=True,help_text="Mark inactive if project got removed")

    def __str__(self):
        return self.project_name
    
class ProjectAttendance(models.Model):
    project = models.ForeignKey(Projects,on_delete=models.CASCADE,related_name="project_attendance")
    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField()
    project_profile = models.ForeignKey(Resource,on_delete=models.PROTECT,help_text="Main profile of the project",related_name="project_profile")
    resources = models.ManyToManyField(Resource,blank=True,related_name="assigned_resources")
    poc = models.ManyToManyField(Resource,blank=True,related_name="assigned_poc")
    present_days = models.FloatField(default=0)
    billable_days = models.FloatField(default=0)
    non_billable_days = models.FloatField(default=0)
    billable_hours = models.FloatField(default=0,help_text="Leave empty to auto-calcuate")
    non_billable_hours = models.FloatField(default=0,help_text="Leave empty to auto-calculate")
    extra_hours = models.FloatField(default=0,null=True,blank=True)

    def save(self,*args, **kwargs):
        if self.billable_hours in (None,0):
            self.billable_hours = self.billable_days * 8
        if self.non_billable_hours in (None,0):
            self.non_billable_hours = self.non_billable_hours * 8

        super.save(*args, **kwargs)

    def __str__(self):
        return self.project.project_name