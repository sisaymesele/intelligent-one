from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from management_project.models import StrategicCycle
from management_project.forms import StrategicCycleForm


@login_required
def strategic_cycle_list(request):
    """
    List all strategic cycles for the current user's organization
    """
    cycles = StrategicCycle.objects.filter(
        organization_name=request.user.organization_name
    ).order_by('start_date')

    context = {
        'strategic_cycles': cycles,
    }
    return render(request, 'strategic_cycle/list.html', context)


# @login_required
# def create_strategic_cycle(request):
#     """
#     Create a new strategic cycle for the user's organization
#     """
#     if request.method == 'POST':
#         form = StrategicCycleForm(request.POST)
#         if form.is_valid():
#             cycle = form.save(commit=False)
#             cycle.organization_name = request.user.organization_name
#             cycle.save()
#             messages.success(request, "Strategic cycle created successfully!")
#             return redirect('strategic_cycle_list')
#     else:
#         form = StrategicCycleForm()
#
#     context = {
#         'form': form,
#         'create_mode': True,
#     }
#     return render(request, 'strategic_cycle/form.html', context)
#
# @login_required
# def create_strategic_cycle(request):
#     """
#     Create a new strategic cycle for the current user's organization.
#     Supports optional 'next' redirect back to parent Strategic Action Plan form.
#     """
#     next_url = request.GET.get("next") or request.POST.get("next")
#
#     if request.method == "POST":
#         form = StrategicCycleForm(request.POST)
#         if form.is_valid():
#             cycle = form.save(commit=False)
#             cycle.organization_name = request.user.organization_name
#             cycle.save()
#             messages.success(request, "Strategic cycle created successfully!")
#
#             # Redirect back to parent form if next_url is provided
#             if next_url:
#                 separator = '&' if '?' in next_url else '?'
#                 return redirect(f"{next_url}{separator}cycle={cycle.pk}")
#
#             return redirect("strategic_cycle_list")  # fallback
#
#     else:
#         form = StrategicCycleForm()
#
#     return render(request, "strategic_cycle/form.html", {
#         "form": form,
#         "next": next_url,
#         "create_mode": True,
#     })

@login_required
def create_strategic_cycle(request):
    next_url = request.GET.get("next") or request.POST.get("next")  # child URL to return to

    if request.method == "POST":
        form = StrategicCycleForm(request.POST)
        if form.is_valid():
            cycle = form.save(commit=False)
            cycle.organization_name = request.user.organization_name
            cycle.save()
            messages.success(request, "Strategic Cycle created successfully!")

            # Redirect back to child form with new cycle preselected
            if next_url:
                separator = '&' if '?' in next_url else '?'
                return redirect(f"{next_url}{separator}cycle={cycle.pk}")

            return redirect("strategic_cycle_list")  # fallback
    else:
        form = StrategicCycleForm()

    return render(request, "strategic_cycle/form.html", {
        "form": form,
        "next": next_url
    })


@login_required
def update_strategic_cycle(request, pk):
    """
    Update an existing strategic cycle
    """
    cycle = get_object_or_404(
        StrategicCycle,
        pk=pk,
        organization_name=request.user.organization_name
    )

    if request.method == 'POST':
        form = StrategicCycleForm(request.POST, instance=cycle)
        if form.is_valid():
            form.save()
            messages.success(request, "Strategic cycle updated successfully!")
            return redirect('strategic_cycle_list')
    else:
        form = StrategicCycleForm(instance=cycle)

    context = {
        'form': form,
        'edit_mode': True,
        'editing_strategic_cycle': cycle,
    }
    return render(request, 'strategic_cycle/form.html', context)


@login_required
def delete_strategic_cycle(request, pk):
    """
    Delete a strategic cycle belonging to the user's organization
    """
    cycle = get_object_or_404(
        StrategicCycle,
        pk=pk,
        organization_name=request.user.organization_name
    )

    if request.method == 'POST':
        cycle.delete()
        messages.success(request, "Strategic cycle deleted successfully!")
        return redirect('strategic_cycle_list')

    context = {
        'strategic_cycle': cycle,
    }
    return render(request, 'strategic_cycle/delete_confirm.html', context)
