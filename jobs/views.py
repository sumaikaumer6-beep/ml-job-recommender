from django.shortcuts import render
from .models import Job
from ml_engine.recommender import get_job_recommendations
# Create your views here.
def job_list(request):
    all_jobs = Job.objects.all()
    user_skills = "Python, Django, SQL"
    if request.user.is_authenticated and hasattr(request.user, 'profile'):
        user_skills = request.user.profile.skills
    recommendations = get_job_recommendations(user_skills,all_jobs)
    return render(request, 'jobs/job_list.html', {
         'recommendations': recommendations,
          'user_skills': user_skills
    })
