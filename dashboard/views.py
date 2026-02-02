from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NGOActivityForm
from .services.activity_service import ActivityService

def create_activity_view(request):
    if request.method == 'POST':
        form = NGOActivityForm(request.POST)
        if form.is_valid():
            #get data from form
            data = form.cleaned_data
            #create activity using service
            ActivityService.create_activity(data)
            messages.success(request, 'Activity created successfully!')
            #redirect to dashboard
            return redirect('dashboard')
    else:
        form = NGOActivityForm()

    return render(request, 'dashboard/create_activity.html', {'form': form}) #return form to template