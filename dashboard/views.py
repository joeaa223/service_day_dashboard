from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import NGOActivityForm
from .services.activity_service import ActivityService
from .models import NGOActivity

def ngo_list_view(request):
    """View to list all NGO activities"""
    activities = ActivityService.get_all_activities()
    return render(request, 'dashboard/ngo_list.html', {'activities': activities})

def create_activity_view(request):
    """View to create a new activity"""
    if request.method == 'POST':
        form = NGOActivityForm(request.POST)
        if form.is_valid():
            ActivityService.create_activity(form.cleaned_data)
            messages.success(request, 'Activity created successfully!')
            return redirect('ngo_list')
    else:
        form = NGOActivityForm()
    return render(request, 'dashboard/ngo_form.html', {'form': form, 'title': 'Create New Activity'})

def update_activity_view(request, pk):
    """View to update an existing activity"""
    activity = get_object_or_404(NGOActivity, pk=pk)
    if request.method == 'POST':
        form = NGOActivityForm(request.POST, instance=activity)
        if form.is_valid():
            ActivityService.update_activity(pk, form.cleaned_data)
            messages.success(request, 'Activity updated successfully!')
            return redirect('ngo_list')
    else:
        form = NGOActivityForm(instance=activity)
    return render(request, 'dashboard/ngo_form.html', {'form': form, 'title': 'Update Activity Details'})

def toggle_activity_status_view(request, pk):
    """View to toggle activity active/inactive status"""
    ActivityService.toggle_activity_status(pk)
    messages.info(request, 'Activity status updated')
    return redirect('ngo_list')