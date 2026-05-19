from django.shortcuts import render, redirect, get_object_or_404
from .models import Job

def home(request):
    return render(request, 'main/home.html')



def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'main/job_list.html', {'jobs': jobs})



def job_detail(request, id):
    job = get_object_or_404(Job, id=id)
    return render(request, 'main/job_detail.html', {'job': job})



def add_job(request):
    if request.method == "POST":
        title = request.POST['title']
        company = request.POST['company']
        description = request.POST['description']
        location = request.POST['location']

        Job.objects.create(
            title=title,
            company=company,
            description=description,
            location=location
        )
        return redirect('job_list')

    return render(request, 'main/add_job.html')




def apply_job(request, id):
    job = get_object_or_404(Job, id=id)

    if request.method == "POST":
        applicant_name = request.POST['name']
        email = request.POST['email']

        return redirect('job_list')

    return render(request, 'main/apply_job.html', {'job': job})