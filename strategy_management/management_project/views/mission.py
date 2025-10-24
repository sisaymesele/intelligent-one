from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from management_project.models import Mission
from management_project.forms import MissionForm
from management_project.services.permissions import role_required, get_user_permissions

# -------------------- MISSION LIST --------------------
@login_required
@role_required(['editor', 'viewer'])  # Both roles can view
def mission_list(request):
    # Show only missions for the user's organization
    missions = Mission.objects.filter(
        organization_name=request.user.organization_name
    ).order_by('-id')

    paginator = Paginator(missions, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Get user permissions
    permissions = get_user_permissions(request.user)

    # Only show form if user has create permission
    form = MissionForm() if permissions.get('mission_create', False) else None

    context = {
        'page_obj': page_obj,
        'form': form,
        'permissions': permissions,
        'edit_mode': False,
    }
    return render(request, 'mission/list.html', context)


# -------------------- CREATE MISSION --------------------
@login_required
@role_required(['editor'])  # Only editor can create
def create_mission(request):
    permissions = get_user_permissions(request.user)
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

    context = {
        'form': form,
        'permissions': permissions,
        'edit_mode': False,
    }
    return render(request, 'mission/list.html', context)


# -------------------- UPDATE MISSION --------------------
@login_required
@role_required(['editor'])  # Only editor can update
def update_mission(request, pk):
    mission = get_object_or_404(
        Mission,
        pk=pk,
        organization_name=request.user.organization_name
    )
    permissions = get_user_permissions(request.user)

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
        'permissions': permissions,
        'edit_mode': True,
        'editing_mission': mission,
    }
    return render(request, 'mission/list.html', context)


# -------------------- DELETE MISSION --------------------
@login_required
@role_required(['editor'])  # Only editor can delete
def delete_mission(request, pk):
    mission = get_object_or_404(
        Mission,
        pk=pk,
        organization_name=request.user.organization_name
    )
    permissions = get_user_permissions(request.user)

    if request.method == 'POST':
        mission.delete()
        messages.success(request, "Mission deleted successfully!")
        return redirect('mission_list')

    context = {
        'mission': mission,
        'permissions': permissions,
    }
    return render(request, 'mission/delete_confirm.html', context)
