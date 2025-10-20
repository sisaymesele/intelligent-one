from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from management_project.models import InitiativeResourceItemReport, InitiativeResourceItemPlan, InitiativePlanning
from management_project.forms import InitiativeResourceItemReportForm

# -------------------- LIST INITIATIVE RESOURCE ITEM REPORTS --------------------
@login_required
def initiative_resource_item_report_list(request):
    query = request.GET.get('search', '').strip()
    selected_initiative = request.GET.get('initiative_name', '').strip()
    page_number = request.GET.get('page', 1)

    # Base queryset: all resource item reports for user's organization
    reports = InitiativeResourceItemReport.objects.filter(
        initiative_resource_plan__organization=request.user.organization_name
    ).select_related('initiative_resource_plan', 'initiative_resource_plan__initiative_name')

    # Filter by selected initiative
    selected_initiative_name = None
    if selected_initiative:
        reports = reports.filter(initiative_resource_plan__initiative_name_id=selected_initiative)
        initiative_obj = InitiativePlanning.objects.filter(pk=selected_initiative).first()
        if initiative_obj:
            selected_initiative_name = initiative_obj.initiative_name

    # Search filter across initiative fields + resource name
    if query:
        reports = reports.filter(
            Q(initiative_resource_plan__initiative_name__initiative_name__icontains=query) |
            Q(initiative_resource_plan__initiative_name__initiative_dimension__icontains=query) |
            Q(initiative_resource_plan__initiative_name__initiative_focus_area__icontains=query) |
            Q(initiative_resource_plan__resource_name__icontains=query) |
            Q(initiative_resource_plan__resource_type__icontains=query)
        )

    # Ordering
    reports = reports.order_by('initiative_resource_plan__initiative_name__initiative_name', 'initiative_resource_plan__resource_name')

    # Pagination
    paginator = Paginator(reports, 10)
    page_obj = paginator.get_page(page_number)

    # Initiative dropdown for filter
    initiatives = InitiativePlanning.objects.filter(
        organization_name=request.user.organization_name
    ).order_by('initiative_name')

    return render(request, 'initiative_resource_item_report/list.html', {
        'reports': page_obj,
        'page_obj': page_obj,
        'search_query': query,
        'initiatives': initiatives,
        'selected_initiative': selected_initiative,
        'selected_initiative_name': selected_initiative_name,
    })


# -------------------- CREATE INITIATIVE RESOURCE ITEM REPORT --------------------

@login_required
def create_initiative_resource_item_report(request):
    next_url = request.GET.get('next') or request.POST.get('next')
    initial_data = {}

    # Preselect parent if passed
    parent_id = request.GET.get('initiative_resource_plan') or request.POST.get('initiative_resource_plan')
    if parent_id:
        initial_data['initiative_resource_plan'] = parent_id

    if request.method == 'POST':
        form = InitiativeResourceItemReportForm(request.POST, request=request)
        if form.is_valid() and 'save' in request.POST:
            report = form.save(commit=False)
            report.save()
            messages.success(request, "Initiative resource item report created successfully!")
            return redirect('initiative_resource_item_report_list')
    else:
        form = InitiativeResourceItemReportForm(initial=initial_data, request=request)

    return render(request, 'initiative_resource_item_report/form.html', {'form': form, 'next': next_url})


# -------------------- UPDATE INITIATIVE RESOURCE ITEM REPORT --------------------
@login_required
def update_initiative_resource_item_report(request, pk):
    report = get_object_or_404(
        InitiativeResourceItemReport,
        pk=pk,
        initiative_resource_plan__organization=request.user.organization_name
    )

    if request.method == 'POST':
        form = InitiativeResourceItemReportForm(request.POST, instance=report, request=request)
        if 'save' in request.POST and form.is_valid():
            form.save()
            messages.success(request, "Initiative resource item report updated successfully!")
            return redirect('initiative_resource_item_report_list')
        else:
            messages.error(request, "Error updating report. Please check the form.")
    else:
        form = InitiativeResourceItemReportForm(instance=report, request=request)

    return render(request, 'initiative_resource_item_report/form.html', {'form': form})


# -------------------- DELETE INITIATIVE RESOURCE ITEM REPORT --------------------
@login_required
def delete_initiative_resource_item_report(request, pk):
    report = get_object_or_404(
        InitiativeResourceItemReport,
        pk=pk,
        initiative_resource_plan__organization=request.user.organization_name
    )

    if request.method == 'POST':
        report.delete()
        messages.success(request, "Initiative resource item report deleted successfully!")
        return redirect('initiative_resource_item_report_list')

    return render(request, 'initiative_resource_item_report/delete_confirm.html', {'report': report})
