# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.utils import timezone
# from django.core.mail import send_mail
# from django.conf import settings
# from django.urls import reverse
# from django.contrib.auth import login
#
# from management_project.models import OrganizationalProfile, OrganizationInvitation
# from account.models import CustomUser
# from management_project.forms import OrganizationInvitationForm
# from account.forms import CustomUserRegistrationForm
#
#
# # ---------------- INVITATION LIST ----------------
# @login_required
# def invitation_list(request):
#     """List all invitations for the current organization (owner only)."""
#     org = get_object_or_404(OrganizationalProfile, owner=request.user)
#     invitations = org.invitations.all().order_by('-created_at')
#     return render(request, 'invitation/list.html', {'organization': org, 'invitations': invitations})
#
#
# # ---------------- SEND INVITATION ----------------
# @login_required
# def send_invitation(request):
#     """Owner sends invitation to join organization."""
#     org = get_object_or_404(OrganizationalProfile, owner=request.user)
#
#     if request.method == 'POST':
#         form = OrganizationInvitationForm(request.POST)
#         if form.is_valid():
#             invitation = form.save(commit=False)
#             invitation.organization = org
#             invitation.invited_by = request.user
#             invitation.save()
#
#             # Build acceptance link using the token
#             accept_url = request.build_absolute_uri(
#                 reverse('accept_invitation_token', args=[invitation.token])
#             )
#
#             send_mail(
#                 subject=f"Invitation to join {org.organization_name}",
#                 message=f"You have been invited to join {org.organization_name} as {invitation.role}.\n"
#                         f"Click here to accept: {accept_url}",
#                 from_email=settings.DEFAULT_FROM_EMAIL,
#                 recipient_list=[invitation.email],
#             )
#
#             messages.success(request, f"Invitation sent to {invitation.email}")
#             return redirect('invitation_list')
#     else:
#         form = OrganizationInvitationForm()
#
#     return render(request, 'invitation/form.html', {'form': form})
#
#
# # ---------------- ACCEPT INVITATION VIA TOKEN ----------------
# def accept_invitation_token(request, token):
#     """Handle accepting an invitation via token link."""
#     invitation = get_object_or_404(OrganizationInvitation, token=token)
#
#     # Already accepted or cancelled?
#     if invitation.status != OrganizationInvitation.PENDING:
#         messages.info(request, "This invitation is no longer valid.")
#         return redirect('swot_analysis_list')
#
#     # Check if user exists
#     try:
#         user = CustomUser.objects.get(email=invitation.email)
#         login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#         # Assign organization if not yet assigned
#         if not getattr(user, 'organization_name', None):
#             user.organization_name = invitation.organization
#             user.save()
#         # Accept invitation
#         invitation.status = OrganizationInvitation.ACCEPTED
#         invitation.responded_at = timezone.now()
#         invitation.save()
#         messages.success(request, f"You have joined {invitation.organization.organization_name} as {invitation.role}")
#         return redirect('swot_analysis_list')
#
#     except CustomUser.DoesNotExist:
#         # User doesn't exist → register
#         if request.method == 'POST':
#             form = CustomUserRegistrationForm(request.POST)
#             if form.is_valid():
#                 user = form.save(commit=False)
#                 user.email = invitation.email  # enforce email
#                 user.organization_name = invitation.organization
#                 user.save()
#                 login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#                 invitation.status = OrganizationInvitation.ACCEPTED
#                 invitation.responded_at = timezone.now()
#                 invitation.save()
#                 messages.success(request, f"Account created and joined {invitation.organization.organization_name} as {invitation.role}")
#                 return redirect('dashboard')
#         else:
#             form = CustomUserRegistrationForm(initial={'email': invitation.email})
#
#         return render(request, 'invitation/register_from_invite.html', {'form': form})
#
#
# # ---------------- CANCEL INVITATION ----------------
# @login_required
# def cancel_invitation(request, pk):
#     """Cancel pending invitation (Owner only)."""
#     invitation = get_object_or_404(OrganizationInvitation, pk=pk, organization__owner=request.user)
#
#     if request.method == 'POST':
#         invitation.status = OrganizationInvitation.CANCELLED
#         invitation.responded_at = timezone.now()
#         invitation.save()
#         messages.success(request, f"Invitation to {invitation.email} cancelled.")
#         return redirect('invitation_list')
#
#     return render(request, 'invitation/cancel_confirm.html', {'invitation': invitation})
#
#
# # ---------------- DELETE INVITATION ----------------
# @login_required
# def delete_invitation(request, pk):
#     """Permanently delete an invitation (Owner only)."""
#     invitation = get_object_or_404(OrganizationInvitation, pk=pk, organization__owner=request.user)
#
#     if request.method == 'POST':
#         invitation.delete()
#         messages.success(request, f"Invitation to {invitation.email} deleted.")
#         return redirect('invitation_list')
#
#     return render(request, 'invitation/delete_confirm.html', {'invitation': invitation})


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import login

from management_project.models import OrganizationalProfile, OrganizationInvitation
from account.models import CustomUser
from management_project.forms import OrganizationInvitationForm
from account.forms import CustomUserRegistrationForm


# ---------------- INVITATION LIST ----------------
@login_required
def invitation_list(request):
    """List all invitations for the current organization (owner only)."""
    org = get_object_or_404(OrganizationalProfile, organization_name=request.user.organization_name)
    invitations = org.invitations.all().order_by('-created_at')
    return render(request, 'invitation/list.html', {'organization': org, 'invitations': invitations})


# ---------------- SEND INVITATION ----------------
@login_required
def send_invitation(request):
    """Owner sends invitation to join organization."""
    org = get_object_or_404(OrganizationalProfile, organization_name=request.user.organization_name)

    if request.method == 'POST':
        form = OrganizationInvitationForm(request.POST)
        if form.is_valid():
            invitation = form.save(commit=False)
            invitation.organization_name = org
            invitation.invited_by = request.user
            invitation.save()

            # Build acceptance link using the token
            accept_url = request.build_absolute_uri(
                reverse('accept_invitation_token', args=[invitation.token])
            )

            send_mail(
                subject=f"Invitation to join {org.organization_name}",
                message=f"You have been invited to join {org.organization_name} as {invitation.role}.\n"
                        f"Click here to accept: {accept_url}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[invitation.email],
            )

            messages.success(request, f"Invitation sent to {invitation.email}")
            return redirect('invitation_list')
    else:
        form = OrganizationInvitationForm()

    return render(request, 'invitation/form.html', {'form': form})


# ---------------- ACCEPT INVITATION VIA TOKEN ----------------



def accept_invitation_token(request, token):
    """Handle accepting an invitation via token link."""
    invitation = get_object_or_404(OrganizationInvitation, token=token)

    # Already accepted or cancelled?
    if invitation.status != OrganizationInvitation.PENDING:
        messages.info(request, "This invitation is no longer valid.")
        return redirect('swot_analysis_list')

    # Check if user exists
    try:
        user = CustomUser.objects.get(email=invitation.email)
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')

        # Assign organization if not yet assigned
        if not getattr(user, 'organization_name', None):
            user.organization_name = invitation.organization_name
            user.save()

        # Accept invitation
        invitation.status = OrganizationInvitation.ACCEPTED
        invitation.responded_at = timezone.now()
        invitation.save()

        messages.success(request, f"You have joined {invitation.organization_name.organization_name} as {invitation.role}")
        return redirect('dashboard')

    except CustomUser.DoesNotExist:
        # User doesn't exist → register
        if request.method == 'POST':
            form = CustomUserRegistrationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.email = invitation.email  # enforce email
                user.organization_name = invitation.organization_name
                user.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')

                invitation.status = OrganizationInvitation.ACCEPTED
                invitation.responded_at = timezone.now()
                invitation.save()

                messages.success(request, f"Account created and joined {invitation.organization_name.organization_name} as {invitation.role}")
                return redirect('dashboard')
        else:
            form = CustomUserRegistrationForm(initial={'email': invitation.email})

        return render(request, 'invitation/register_from_invite.html', {'form': form})


# ---------------- CANCEL INVITATION ----------------
@login_required
def cancel_invitation(request, pk):
    """Cancel pending invitation (Owner only)."""
    invitation = get_object_or_404(
        OrganizationInvitation,
        pk=pk,
        organization_name__organization_name=request.user.organization_name
    )

    if request.method == 'POST':
        invitation.status = OrganizationInvitation.CANCELLED
        invitation.responded_at = timezone.now()
        invitation.save()
        messages.success(request, f"Invitation to {invitation.email} cancelled.")
        return redirect('invitation_list')

    return render(request, 'invitation/cancel_confirm.html', {'invitation': invitation})


# ---------------- DELETE INVITATION ----------------
@login_required
def delete_invitation(request, pk):
    """Permanently delete an invitation (Owner only)."""
    invitation = get_object_or_404(
        OrganizationInvitation,
        pk=pk,
        organization_name__organization_name=request.user.organization_name
    )

    if request.method == 'POST':
        invitation.delete()
        messages.success(request, f"Invitation to {invitation.email} deleted.")
        return redirect('invitation_list')

    return render(request, 'invitation/delete_confirm.html', {'invitation': invitation})
