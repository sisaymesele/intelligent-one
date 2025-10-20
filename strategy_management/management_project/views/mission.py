from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from management_project.models import Mission
from management_project.forms import MissionForm
from django.core.paginator import Paginator

# -------------------- MISSION LIST --------------------
@login_required
def mission_list(request):
    """
    List all missions for the logged-in user's organization.
    Superusers see all missions.
    """
    if request.user.is_superuser:
        missions = Mission.objects.all().order_by('-id')
    else:
        missions = Mission.objects.filter(organization_name=request.user.organization_name)

    paginator = Paginator(missions, 10)  # 10 missions per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    form = MissionForm()  # Empty form for creating new missions

    context = {
        'page_obj': page_obj,
        'form': form,
    }
    return render(request, 'mission/list.html', context)


# -------------------- CREATE MISSION --------------------
@login_required
def create_mission(request):
    if request.method == 'POST':
        form = MissionForm(request.POST)
        if form.is_valid():
            mission = form.save(commit=False)
            mission.organization_name = request.user.organization_name
            mission.save()
            messages.success(request, "Mission created successfully!")
            return redirect('mission_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = MissionForm()

    return render(request, 'mission/list.html', {'form': form})


# -------------------- UPDATE MISSION --------------------
@login_required
def update_mission(request, pk):
    mission = get_object_or_404(
        Mission,
        pk=pk,
        organization_name=request.user.organization_name
    )

    if request.method == 'POST':
        form = MissionForm(request.POST, instance=mission)
        if form.is_valid():
            form.save()
            messages.success(request, "Mission updated successfully!")
            return redirect('mission_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = MissionForm(instance=mission)

    context = {
        'form': form,
        'edit_mode': True,
        'editing_mission': mission,
    }
    return render(request, 'mission/list.html', context)


# -------------------- DELETE MISSION --------------------
@login_required
def delete_mission(request, pk):
    mission = get_object_or_404(
        Mission,
        pk=pk,
        organization_name=request.user.organization_name
    )

    if request.method == 'POST':
        mission.delete()
        messages.success(request, "Mission deleted successfully!")
        return redirect('mission_list')  # after deletion, redirect to main list

    # GET → show confirmation page
    return render(request, 'mission/delete_confirm.html', {'mission': mission})
