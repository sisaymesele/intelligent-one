from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from management_project.models import Values
from management_project.forms import ValuesForm


# -------------------- VALUES LIST --------------------
@login_required
def values_list(request):
    values = Values.objects.filter(
        organization_name=request.user.organization_name
    ).order_by('-id')

    form = ValuesForm()  # Empty form for creating new values

    context = {
        'values': values,
        'form': form,
    }
    return render(request, 'values/list.html', context)


# -------------------- CREATE VALUES --------------------
@login_required
def create_values(request):
    if request.method == 'POST':
        form = ValuesForm(request.POST)
        if form.is_valid():
            value = form.save(commit=False)
            value.organization_name = request.user.organization_name
            value.save()
            messages.success(request, "Value created successfully!")
            return redirect('values_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ValuesForm()

    return render(request, 'values/list.html', {'form': form})


# -------------------- UPDATE VALUES --------------------
@login_required
def update_values(request, pk):
    value = get_object_or_404(
        Values,
        pk=pk,
        organization_name=request.user.organization_name
    )

    if request.method == 'POST':
        form = ValuesForm(request.POST, instance=value)
        if form.is_valid():
            form.save()
            messages.success(request, "Value updated successfully!")
            return redirect('values_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ValuesForm(instance=value)

    context = {
        'form': form,
        'edit_mode': True,
        'editing_value': value,
    }
    return render(request, 'values/list.html', context)


# -------------------- DELETE VALUES --------------------
@login_required
def delete_values(request, pk):
    value = get_object_or_404(
        Values,
        pk=pk,
        organization_name=request.user.organization_name
    )

    if request.method == 'POST':
        value.delete()
        messages.success(request, "Value deleted successfully!")
        return redirect('values_list')  # after deletion, redirect to main list

    # GET → show confirmation page
    return render(request, 'values/delete_confirm.html', {'value': value})
