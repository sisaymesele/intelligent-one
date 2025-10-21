from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

from management_project.models import RiskManagement
from management_project.forms import RiskManagementForm


# -------------------- LIST --------------------
@login_required
def risk_management_list(request):
    query = request.GET.get('search', '').strip()
    selected_status = request.GET.get('status', '').strip()
    page_number = request.GET.get('page', 1)

    risks = RiskManagement.objects.filter(organization_name=request.user.organization_name)

    if selected_status:
        risks = risks.filter(status=selected_status)

    if query:
        risks = risks.filter(
            Q(risk_category__icontains=query) |
            Q(risk_name__icontains=query) |
            Q(mitigation_action__icontains=query)
        )

    risks = risks.order_by('risk_category', '-created_at')
    status_choices = [choice[0] for choice in RiskManagement.STATUS_CHOICES]

    paginator = Paginator(risks, 10)
    page_obj = paginator.get_page(page_number)

    return render(request, 'risk_management/list.html', {
        'risks': page_obj,
        'page_obj': page_obj,
        'search_query': query,
        'status_choices': status_choices,
        'selected_status': selected_status,
    })


# -------------------- CREATE --------------------
# @login_required
# def create_risk_management(request):
#     if request.method == 'POST':
#         form = RiskManagementForm(request.POST, request=request)
#         if form.is_valid():
#             risk_entry = form.save(commit=False)
#             risk_entry.organization_name = request.user.organization_name
#             risk_entry.save()
#             messages.success(request, "Risk entry created successfully!")
#             return redirect('risk_management_list')
#         else:
#             messages.error(request, "Please fix the errors below.")
#     else:
#         form = RiskManagementForm(request=request)
#
#     return render(request, 'risk_management/form.html', {'form': form})

@login_required
def create_risk_management(request):
    """
    Create a new RiskManagement entry.
    Allows cascading dropdowns to work without saving until Save is clicked.
    """
    if request.method == 'POST':
        # Pass request to form to allow filtering if needed
        form = RiskManagementForm(request.POST, request=request)

        # Only save if 'save' button was clicked
        if 'save' in request.POST:
            if form.is_valid():
                risk_entry = form.save(commit=False)
                risk_entry.organization_name = request.user.organization_name
                risk_entry.save()
                messages.success(request, "Risk entry created successfully!")
                return redirect('risk_management_list')
            else:
                messages.error(request, "Please fix the errors below.")
        # Else: just re-render the form (dropdown changed)
    else:
        form = RiskManagementForm(request=request)

    return render(request, 'risk_management/form.html', {'form': form})


# -------------------- UPDATE --------------------
# -------------------- UPDATE --------------------
@login_required
def update_risk_management(request, pk):
    """
    Update an existing RiskManagement entry.
    Cascading dropdowns still work without saving until Save is clicked.
    """
    entry = get_object_or_404(RiskManagement, pk=pk, organization_name=request.user.organization_name)

    if request.method == 'POST':
        form = RiskManagementForm(request.POST, instance=entry, request=request)

        # Only save if the Save button was clicked
        if 'save' in request.POST:
            if form.is_valid():
                form.save()
                messages.success(request, "Risk entry updated successfully!")
                return redirect('risk_management_list')
            else:
                messages.error(request, "Please fix the errors below.")
        # Else: just re-render the form for cascading dropdowns
    else:
        form = RiskManagementForm(instance=entry, request=request)

    return render(request, 'risk_management/form.html', {'form': form})



# -------------------- DELETE --------------------
@login_required
def delete_risk_management(request, pk):
    entry = get_object_or_404(RiskManagement, pk=pk, organization_name=request.user.organization_name)

    if request.method == 'POST':
        entry.delete()
        messages.success(request, "Risk entry deleted successfully!")
        return redirect('risk_management_list')

    return render(request, 'risk_management/delete_confirm.html', {'entry': entry})
