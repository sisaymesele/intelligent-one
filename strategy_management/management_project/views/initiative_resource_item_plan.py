from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from management_project.models import InitiativeResourceItemPlan, InitiativePlanning
from management_project.forms import InitiativeResourceItemPlanForm

# -------------------- LIST INITIATIVE RESOURCE ITEM PLANS --------------------
@login_required
def initiative_resource_item_plan_list(request):
    query = request.GET.get('search', '').strip()
    selected_initiative = request.GET.get('initiative_name', '').strip()
    page_number = request.GET.get('page', 1)

    # Base queryset: all resource item plans in the user's organization
    resource_item_plans = InitiativeResourceItemPlan.objects.filter(
        organization=request.user.organization_name
    ).select_related('initiative_name')

    # Filter by selected initiative
    selected_initiative_name = None
    if selected_initiative:
        resource_item_plans = resource_item_plans.filter(initiative_name_id=selected_initiative)
        initiative_obj = InitiativePlanning.objects.filter(pk=selected_initiative).first()
        if initiative_obj:
            selected_initiative_name = initiative_obj.initiative_name

    # Search filter across initiative fields + resource_type
    if query:
        resource_item_plans = resource_item_plans.filter(
            Q(initiative_name__initiative_name__icontains=query) |
            Q(initiative_name__initiative_dimension__icontains=query) |
            Q(initiative_name__initiative_focus_area__icontains=query) |
            Q(resource_type__icontains=query)
        )

    # Ordering
    resource_item_plans = resource_item_plans.order_by('initiative_name__initiative_name', 'resource_type')

    # Pagination
    paginator = Paginator(resource_item_plans, 10)
    page_obj = paginator.get_page(page_number)

    # Initiative dropdown for filter
    initiatives = InitiativePlanning.objects.filter(
        organization_name=request.user.organization_name
    ).order_by('initiative_name')

    return render(request, 'initiative_resource_item_plan/list.html', {
        'resource_item_plans': page_obj,
        'page_obj': page_obj,
        'search_query': query,
        'initiatives': initiatives,
        'selected_initiative': selected_initiative,
        'selected_initiative_name': selected_initiative_name,
    })


# -------------------- CREATE INITIATIVE RESOURCE ITEM PLAN --------------------
@login_required
def create_initiative_resource_item_plan(request):
    next_url = request.GET.get('next') or request.POST.get('next')
    if request.method == 'POST':
        form = InitiativeResourceItemPlanForm(request.POST, request=request)
        if form.is_valid() and 'save' in request.POST:
            resource_item_plan = form.save(commit=False)
            resource_item_plan.organization = request.user.organization_name
            resource_item_plan.save()
            messages.success(request, "Initiative resource item plan created successfully!")

            # Redirect back to child form with preselected value
            if next_url:
                return redirect(f"{next_url}?initiative_resource_plan={resource_item_plan.pk}")
            return redirect('initiative_resource_item_plan_list')
    else:
        initial_data = {}
        selected_initiative = request.GET.get('initiative_name')
        if selected_initiative:
            initial_data['initiative_name'] = selected_initiative
        form = InitiativeResourceItemPlanForm(initial=initial_data, request=request)

    return render(request, 'initiative_resource_item_plan/form.html', {'form': form, 'next': next_url})


# -------------------- UPDATE INITIATIVE RESOURCE ITEM PLAN --------------------
@login_required
def update_initiative_resource_item_plan(request, pk):
    resource_item_plan = get_object_or_404(
        InitiativeResourceItemPlan,
        pk=pk,
        organization=request.user.organization_name
    )

    if request.method == 'POST':
        form = InitiativeResourceItemPlanForm(request.POST, instance=resource_item_plan, request=request)
        if 'save' in request.POST and form.is_valid():
            form.save()
            messages.success(request, "Initiative resource item plan updated successfully!")
            return redirect('initiative_resource_item_plan_list')
        else:
            messages.error(request, "Error updating resource item plan. Please check the form.")
    else:
        form = InitiativeResourceItemPlanForm(instance=resource_item_plan, request=request)

    return render(request, 'initiative_resource_item_plan/form.html', {'form': form})


# -------------------- DELETE INITIATIVE RESOURCE ITEM PLAN --------------------
@login_required
def delete_initiative_resource_item_plan(request, pk):
    resource_item_plan = get_object_or_404(
        InitiativeResourceItemPlan,
        pk=pk,
        organization=request.user.organization_name
    )

    if request.method == 'POST':
        resource_item_plan.delete()
        messages.success(request, "Initiative resource item plan deleted successfully!")
        return redirect('initiative_resource_item_plan_list')

    return render(request, 'initiative_resource_item_plan/delete_confirm.html', {'resource_item_plan': resource_item_plan})
