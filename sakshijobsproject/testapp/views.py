from django.shortcuts import render
from testapp.models import HydJobs,PuneJobs,BangJobs

# Create your views here.
def homepage_view(request):
    return render(request,'testapp/index.html')

def hydjobsinfo_views(request):
    jobs_list = HydJobs.objects.all()
    my_dict = {'jobs_list': jobs_list}
    return render(request,'testapp/hydjobs.html',my_dict)

def puneinfo_views(request):
    jobs_list = PuneJobs.objects.all()
    my_dict = {'jobs_list': jobs_list}
    return render(request,'testapp/punejobs.html',my_dict)

def bangjobs_views(request):
    jobs_list = BangJobs.objects.all()
    my_dict = {'jobs_list': jobs_list}
    return render(request,'testapp/bangjobs.html',my_dict)

