# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
# from management_project.models import Vision
# from management_project.forms import VisionForm
# from management_project.services.permissions import role_required
#
# # -------------------- VISION LIST --------------------
# @login_required
# @role_required(['editor', 'viewer'])  # Both editors and viewers can see
# def vision_list(request):
#     visions = Vision.objects.filter(
#         organization_name=request.user.organization_name
#     ).order_by('-id')
#
#     # Only editors can create
#     can_create = getattr(request.user, 'role', None) == 'editor'
#     form = VisionForm() if can_create else None
#
#     context = {
#         'visions': visions,
#         'form': form,
#         'can_create': can_create,
#     }
#     return render(request, 'vision/list.html', context)
#
#
# # -------------------- CREATE VISION --------------------
# @login_required
# @role_required(['editor'])  # Only editor can create
# def create_vision(request):
#     if request.method == 'POST':
#         form = VisionForm(request.POST)
#         if form.is_valid():
#             vision = form.save(commit=False)
#             vision.organization_name = request.user.organization_name
#             vision.save()
#             messages.success(request, "Vision created successfully!")
#             return redirect('vision_list')
#         else:
#             messages.error(request, "Please correct the errors below.")
#     else:
#         form = VisionForm()
#
#     return render(request, 'vision/list.html', {'form': form, 'edit_mode': False})
#
#
# # -------------------- UPDATE VISION --------------------
# @login_required
# @role_required(['editor'])  # Only editor can update
# def update_vision(request, pk):
#     vision = get_object_or_404(Vision, pk=pk, organization_name=request.user.organization_name)
#
#     if request.method == 'POST':
#         form = VisionForm(request.POST, instance=vision)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Vision updated successfully!")
#             return redirect('vision_list')
#         else:
#             messages.error(request, "Please correct the errors below.")
#     else:
#         form = VisionForm(instance=vision)
#
#     return render(request, 'vision/list.html', {
#         'form': form,
#         'edit_mode': True,
#         'editing_vision': vision,
#     })
#
#
# # -------------------- DELETE VISION --------------------
# @login_required
# @role_required(['editor'])  # Only editor can delete
# def delete_vision(request, pk):
#     vision = get_object_or_404(Vision, pk=pk, organization_name=request.user.organization_name)
#
#     if request.method == 'POST':
#         vision.delete()
#         messages.success(request, "Vision deleted successfully!")
#         return redirect('vision_list')
#
#     return render(request, 'vision/delete_confirm.html', {'vision': vision})


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from management_project.models import Vision
from management_project.forms import VisionForm
from management_project.services.permissions import role_required, get_user_permissions

# -------------------- VISION LIST --------------------
@login_required
@role_required(['editor', 'viewer'])  # Both editors and viewers can see
def vision_list(request):
    visions = Vision.objects.filter(
        organization_name=request.user.organization_name
    ).order_by('-id')

    # Get permissions for the logged-in user
    permissions = get_user_permissions(request.user)

    # Only show form if user has create permission
    form = VisionForm() if permissions.get('vision_create', False) else None

    context = {
        'visions': visions,
        'form': form,
        'permissions': permissions,
        'edit_mode': False,
    }
    return render(request, 'vision/list.html', context)


# -------------------- CREATE VISION --------------------
@login_required
@role_required(['editor'])  # Only editor can create
def create_vision(request):
    permissions = get_user_permissions(request.user)
    if request.method == 'POST':
        form = VisionForm(request.POST)
        if form.is_valid():
            vision = form.save(commit=False)
            vision.organization_name = request.user.organization_name
            vision.save()
            messages.success(request, "Vision created successfully!")
            return redirect('vision_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = VisionForm()

    context = {
        'form': form,
        'permissions': permissions,
        'edit_mode': False,
    }
    return render(request, 'vision/list.html', context)


# -------------------- UPDATE VISION --------------------
@login_required
@role_required(['editor'])  # Only editor can update
def update_vision(request, pk):
    vision = get_object_or_404(Vision, pk=pk, organization_name=request.user.organization_name)
    permissions = get_user_permissions(request.user)

    if request.method == 'POST':
        form = VisionForm(request.POST, instance=vision)
        if form.is_valid():
            form.save()
            messages.success(request, "Vision updated successfully!")
            return redirect('vision_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = VisionForm(instance=vision)

    context = {
        'form': form,
        'permissions': permissions,
        'edit_mode': True,
        'editing_vision': vision,
    }
    return render(request, 'vision/list.html', context)


# -------------------- DELETE VISION --------------------
@login_required
@role_required(['editor'])  # Only editor can delete
def delete_vision(request, pk):
    vision = get_object_or_404(Vision, pk=pk, organization_name=request.user.organization_name)
    permissions = get_user_permissions(request.user)

    if request.method == 'POST':
        vision.delete()
        messages.success(request, "Vision deleted successfully!")
        return redirect('vision_list')

    context = {
        'vision': vision,
        'permissions': permissions,
    }
    return render(request, 'vision/delete_confirm.html', context)
