from django.shortcuts import render, redirect, get_object_or_404
from management_project.models import StrategyHierarchy
from management_project.forms import StrategyHierarchyForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages


@login_required
def strategy_hierarchy_list(request):
    """
    List all strategy hierarchy entries belonging to the current user's organization,
    with optional search on perspective, pillar, and objective.
    """
    # Base queryset filtered by user's organization
    strategies = StrategyHierarchy.objects.filter(
        organization_name=request.user.organization_name
    )

    # Get search query
    query = request.GET.get('q', '')
    if query:
        strategies = strategies.filter(
            Q(strategic_perspective__icontains=query) |
            Q(focus_area__icontains=query) |
            Q(objective__icontains=query)
        )

    return render(request, 'strategy_hierarchy/list.html', {
        'strategies': strategies,
        'query': query,  # pass back search term to template
    })


# @login_required
# def create_strategy_hierarchy(request):
#     """
#     Create a new strategy hierarchy entry for the current user's organization.
#     """
#     if request.method == 'POST':
#         form = StrategyHierarchyForm(request.POST)
#         if 'save' in request.POST and form.is_valid():
#             strategy = form.save(commit=False)
#             strategy.organization_name = request.user.organization_name
#             strategy.save()
#             return redirect('strategy_hierarchy_list')
#     else:
#         form = StrategyHierarchyForm()
#
#     return render(request, 'strategy_hierarchy/form.html', {'form': form})

# @login_required
# def create_strategy_hierarchy(request):
#     """
#     Create a new strategy hierarchy entry for the current user's organization.
#     Supports optional 'next' redirect back to Strategic Action Plan page.
#     """
#     next_url = request.GET.get('next') or request.POST.get('next')  # check GET and POST
#
#     if request.method == 'POST':
#         form = StrategyHierarchyForm(request.POST)
#         if 'save' in request.POST and form.is_valid():
#             strategy = form.save(commit=False)
#             strategy.organization_name = request.user.organization_name
#             strategy.save()
#             # Redirect to 'next' if provided, otherwise to hierarchy list
#             return redirect(next_url or 'strategy_hierarchy_list')
#     else:
#         form = StrategyHierarchyForm()
#
#     return render(request, 'strategy_hierarchy/form.html', {
#         'form': form,
#         'next': next_url,
#     })

@login_required
def create_strategy_hierarchy(request):
    """
    Create a new strategy hierarchy entry for the current user's organization.
    Supports optional 'next' redirect back to Strategic Action Plan page with preselected value.
    """
    next_url = request.GET.get('next') or request.POST.get('next')  # URL to return to child

    if request.method == 'POST':
        form = StrategyHierarchyForm(request.POST)
        if 'save' in request.POST and form.is_valid():
            strategy = form.save(commit=False)
            strategy.organization_name = request.user.organization_name
            strategy.save()
            messages.success(request, "Strategy hierarchy created successfully!")

            # Redirect back to child form with new hierarchy preselected
            if next_url:
                separator = '&' if '?' in next_url else '?'
                return redirect(f"{next_url}{separator}strategy_hierarchy={strategy.pk}")

            return redirect('strategy_hierarchy_list')  # fallback to parent list
    else:
        form = StrategyHierarchyForm()

    return render(request, 'strategy_hierarchy/form.html', {
        'form': form,
        'next': next_url,
    })


@login_required
def update_strategy_hierarchy(request, pk):
    """
    Update an existing strategy hierarchy entry, only if it belongs to the user's organization.
    """
    entry = get_object_or_404(
        StrategyHierarchy,
        pk=pk,
        organization_name=request.user.organization_name
    )
    if request.method == 'POST':
        form = StrategyHierarchyForm(request.POST, instance=entry)
        if 'save' in request.POST and form.is_valid():
            form.save()
            return redirect('strategy_hierarchy_list')
    else:
        form = StrategyHierarchyForm(instance=entry)

    return render(request, 'strategy_hierarchy/form.html', {'form': form})


@login_required
def delete_strategy_hierarchy(request, pk):
    """
    Delete an existing strategy hierarchy entry, only if it belongs to the user's organization.
    """
    entry = get_object_or_404(
        StrategyHierarchy,
        pk=pk,
        organization_name=request.user.organization_name
    )
    if request.method == 'POST':
        entry.delete()
        return redirect('strategy_hierarchy_list')

    return render(request, 'strategy_hierarchy/delete_confirm.html', {'entry': entry})
