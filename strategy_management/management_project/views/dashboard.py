from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from management_project.models import OrganizationalProfile, OrganizationInvitation
from management_project.services.permissions import role_required, get_user_permissions
from django.contrib.auth import get_user_model

#
# @login_required
# def dashboard(request):
#     has_company = OrganizationalProfile.objects.filter(organization_name=request.user.organization_name).exists()
#
#     if not has_company:
#         return redirect('create_organizational_profile')
#
#     return render(request, 'dashboard.html')
#


@login_required
def dashboard(request):
    # Ensure the user belongs to an organization
    has_company = OrganizationalProfile.objects.filter(
        organization_name=request.user.organization_name
    ).exists()

    if not has_company:
        return redirect('create_organizational_profile')

    # Get permissions for template
    permissions = get_user_permissions(request.user)

    return render(request, 'dashboard.html', {
        'permissions': permissions
    })