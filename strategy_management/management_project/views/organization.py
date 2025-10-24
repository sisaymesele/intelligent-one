# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from management_project.models import OrganizationalProfile, OrganizationInvitation
# from management_project.forms import OrganizationalProfileForm
# from management_project.services.permissions import role_required
# from django.http import HttpResponseForbidden
#
# # -----------------------
# # List Organizational Profiles
# # -----------------------
# @login_required
# @role_required(['editor'])
#
# def organizational_profile(request):
#     # Only show profiles the user belongs to
#     invitations = OrganizationInvitation.objects.filter(
#         email=request.user.email, status='accepted'
#     )
#     organizational_profiles = [inv.organization for inv in invitations]
#
#     context = {'organizational_profiles': organizational_profiles}
#     return render(request, 'organizational_profile/list.html', context)
#
#
# # -----------------------
# # Create Organization
# # -----------------------
# @login_required
# def create_organizational_profile(request):
#     # Prevent creating if user already has an accepted invitation
#     existing_invitation = OrganizationInvitation.objects.filter(
#         email=request.user.email, status='accepted'
#     ).first()
#     if existing_invitation:
#         messages.info(request, "You already belong to an organization.")
#         return redirect('dashboard')
#
#     if request.method == 'POST':
#         form = OrganizationalProfileForm(request.POST)
#         if form.is_valid():
#             org = form.save()
#             # Automatically create invitation for creator
#             OrganizationInvitation.objects.create(
#                 organization=org,
#                 email=request.user.email,
#                 role='editor',  # Or owner if you implement owner role
#                 invited_by=request.user,
#                 status='accepted'
#             )
#             messages.success(request, "Organization created successfully.")
#             return redirect('dashboard')
#         else:
#             messages.error(request, "Please correct the errors below.")
#     else:
#         form = OrganizationalProfileForm()
#
#     return render(request, 'organizational_profile/form.html', {'form': form})
#
#
# # -----------------------
# # Update Organization
# # -----------------------
# @login_required
# @role_required(['editor'])  # Only editor/owner can update
# def update_organizational_profile(request, pk):
#     invitation = OrganizationInvitation.objects.filter(
#         email=request.user.email, status='accepted'
#     ).first()
#     if not invitation:
#         return HttpResponseForbidden("You cannot edit this organization.")
#
#     organizational_profile = get_object_or_404(
#         OrganizationalProfile, pk=pk, id=invitation.organization.id
#     )
#
#     if request.method == 'POST':
#         form = OrganizationalProfileForm(request.POST, instance=organizational_profile)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Organizational Profile updated successfully!")
#             return redirect('organizational_profile')
#         else:
#             messages.error(request, "Please correct the errors below.")
#     else:
#         form = OrganizationalProfileForm(instance=organizational_profile)
#
#     context = {
#         'form': form,
#         'edit_mode': True,
#         'editing_profile': organizational_profile,
#     }
#     return render(request, 'organizational_profile/form.html', context)
#
#
# # -----------------------
# # Delete Organization
# # -----------------------
# @login_required
# @role_required(['editor'])  # Only editor/owner can delete
# def delete_organizational_profile(request, pk):
#     invitation = OrganizationInvitation.objects.filter(
#         email=request.user.email, status='accepted'
#     ).first()
#     if not invitation:
#         return HttpResponseForbidden("You cannot delete this organization.")
#
#     profile = get_object_or_404(
#         OrganizationalProfile, pk=pk, id=invitation.organization.id
#     )
#
#     if request.method == 'POST':
#         profile.delete()
#         messages.success(request, "Organizational Profile deleted successfully!")
#         return redirect("organizational_profile")
#
#     return render(request, "organizational_profile/delete_confirm.html", {"profile": profile})


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from management_project.models import OrganizationalProfile, OrganizationInvitation
from management_project.forms import OrganizationalProfileForm
from management_project.services.permissions import role_required, get_user_permissions
from django.http import HttpResponseForbidden

# --------------------
# List Organizational Profiles
# --------------------
@login_required
@role_required(['editor', 'viewer'])
def organizational_profile(request):
    permissions = get_user_permissions(request.user)

    # Only show profiles for the user's organization
    organizational_profiles = OrganizationalProfile.objects.filter(
        organization_name=request.user.organization_name
    )

    context = {
        'organizational_profiles': organizational_profiles,
        'permissions': permissions,
    }
    return render(request, 'organizational_profile/list.html', context)


# --------------------
# Create Organization
# --------------------
@login_required
def create_organizational_profile(request):
    permissions = get_user_permissions(request.user)

    # Prevent creating if user already belongs to an accepted invitation
    if OrganizationInvitation.objects.filter(email=request.user.email, status='accepted').exists():
        messages.info(request, "You already belong to an organization.")
        return redirect('dashboard')

    if request.method == 'POST':
        form = OrganizationalProfileForm(request.POST)
        if form.is_valid():
            org = form.save()

            # Assign user to this organization
            request.user.organization_name = org
            request.user.save()

            # Automatically create invitation for creator as editor
            OrganizationInvitation.objects.create(
                organization_name=org,
                email=request.user.email,
                role='editor',
                invited_by=request.user,
                status=OrganizationInvitation.ACCEPTED
            )

            messages.success(request, "Organization created successfully. You are assigned as Editor.")
            return redirect('dashboard')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = OrganizationalProfileForm()

    context = {
        'form': form,
        'permissions': permissions,
        'edit_mode': False,
    }
    return render(request, 'organizational_profile/form.html', context)


# --------------------
# Update Organization
# --------------------
@login_required
def update_organizational_profile(request, pk):
    permissions = get_user_permissions(request.user)

    # Ensure user can only update their organization
    organizational_profile = get_object_or_404(
        OrganizationalProfile, pk=pk, organization_name=request.user.organization_name
    )

    if request.method == 'POST':
        form = OrganizationalProfileForm(request.POST, instance=organizational_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Organizational Profile updated successfully!")
            return redirect('organizational_profile')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = OrganizationalProfileForm(instance=organizational_profile)

    context = {
        'form': form,
        'permissions': permissions,
        'edit_mode': True,
        'editing_profile': organizational_profile,
    }
    return render(request, 'organizational_profile/form.html', context)


# --------------------
# Delete Organization
# --------------------
@login_required
def delete_organizational_profile(request, pk):
    permissions = get_user_permissions(request.user)

    # Ensure user can only delete their organization
    profile = get_object_or_404(
        OrganizationalProfile, pk=pk, organization_name=request.user.organization_name
    )

    if request.method == "POST":
        profile.delete()
        messages.success(request, "Organizational Profile deleted successfully!")
        return redirect("organizational_profile")

    context = {
        'profile': profile,
        'permissions': permissions,
    }
    return render(request, "organizational_profile/delete_confirm.html", context)
