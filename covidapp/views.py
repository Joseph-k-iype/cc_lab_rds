from django.shortcuts import render, redirect
from .forms import CovidForm
from .models import *

# Create your views here.

def covid(request):
    form = CovidForm()
    if request.method == 'POST':
        form = CovidForm(request.POST)
        if form.is_valid():
            form.save()
            form = CovidForm()
            redirect('covid_dash')
    context = {'form': form}
    return render(request, 'covid_upload.html', context)

# get covid_details from database and pass it to covid_dash.html
def covid_dash(request):
    covid_details = Covid_details.objects.all()
    # get all the states from the database
    states = Covid_details.objects.values_list('state_name', flat=True).distinct()
    # get the total number of samples collected by iterating through the database
    total_samples = 0
    for i in covid_details:
        total_samples += i.No_of_samples
        #get count of total_samples
    total_samples_count = covid_details.count()

    # get the total number of deaths by iterating through the database
    total_deaths = 0
    for i in covid_details:
        total_deaths += i.no_of_deaths
    
    context = {'covid_details': covid_details, 'states': states, 'total_samples_count': total_samples_count, 'total_deaths': total_deaths}
    return render(request, 'covid_dash.html', context)
    