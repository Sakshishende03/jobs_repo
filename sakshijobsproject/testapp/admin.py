from django.contrib import admin
from testapp.models import HydJobs,PuneJobs,BangJobs

# Register your models here.
class HydJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','address','email','phonenumber']
admin.site.register(HydJobs,HydJobsAdmin)

class PuneJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','address','email','phonenumber']
admin.site.register(PuneJobs,PuneJobsAdmin)

class BangJobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','address','email','phonenumber']
admin.site.register(BangJobs,BangJobsAdmin)