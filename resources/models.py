from django.db import models
import calendar

class Resource(models.Model):
    resource_name = models.CharField(max_length=100,help_text="Full name of resource")
    join_date = models.DateField(help_text="Date the resource joined")
    leave_date = models.DateField(null=True,blank=True,help_text="Date the resource left(optional)")
    is_active = models.BooleanField(default=True,help_text="Mark inactive if resource left")

    def __str__(self):
        return self.resource_name
    
class ResourceAttendace(models.Model):
    resource = models.ForeignKey(Resource,on_delete=models.CASCADE,related_name="resource_attendance")
    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField()
    working_days = models.FloatField(null=True,blank=True,help_text="Leave empty to auto-calculate")
    present_day = models.FloatField(default=0)
    present_hours = models.FloatField(default=0,help_text="Leave empty to auto-calculate")

    def save(self,*args,**kwargs):
        if self.working_days in (None,0):
            total_days = calendar.monthrange(self.year,self.month)[1]
            self.working_days = total_days - 7
        if self.present_hours in (None,0):
            self.present_hours = self.present_day * 8
        
        super.save(*args, **kwargs)

    def __str__(self):
        return self.resource.resource_name