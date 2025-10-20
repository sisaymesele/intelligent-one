from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from management_project.models import OrganizationalProfile


# @login_required
# def dashboard(request):
#     # Check if the user has a related organizational profile
#     has_company = OrganizationalProfile.objects.filter(organization_name=request.user.organization_name).exists()
#
#     if not has_company:
#         return redirect('create_organizational_profile')
#
#     return render(request, 'dashboard.html')


@login_required
def dashboard(request):
    # Fetch the organization owned by the user
    try:
        org = OrganizationalProfile.objects.get(owner=request.user)
    except OrganizationalProfile.DoesNotExist:
        # Redirect to create org if none exists
        return redirect('create_organizational_profile')

    context = {'organization': org}
    return render(request, 'dashboard.html', context)