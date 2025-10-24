from functools import wraps
from django.http import HttpResponseForbidden
from django.contrib.auth import get_user_model
from management_project.models import OrganizationInvitation
from django.contrib import messages

# -------------------- Decorator --------------------


def role_required(allowed_roles):
    """Restrict access based on accepted invitation role."""

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            # Safely get user's organization
            org = getattr(request.user, 'organization_name', None)

            if not org:
                return HttpResponseForbidden("You do not have permission to access this page.")

            # Check accepted invitation for this organization
            invitation = OrganizationInvitation.objects.filter(
                email=request.user.email,
                organization_name=org,
                status=OrganizationInvitation.ACCEPTED
            ).first()

            if not invitation:
                return HttpResponseForbidden("You do not have permission to access this page.")

            if invitation.role not in allowed_roles:
                return HttpResponseForbidden("You do not have permission to access this page.")

            return view_func(request, *args, **kwargs)

        return _wrapped_view
    return decorator

def role_required_invitation(allowed_roles):
    """Restrict access for invitation views, fallback to user role if no invitation."""

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            org = getattr(request.user, 'organization_name', None)
            if not org:
                return HttpResponseForbidden("You do not have permission to access this page.")

            # Try to find accepted invitation
            invitation = OrganizationInvitation.objects.filter(
                email=request.user.email,
                organization_name=org,
                status=OrganizationInvitation.ACCEPTED
            ).first()

            # If no invitation, fallback to checking if user is staff/editor
            role = invitation.role if invitation else getattr(request.user, 'role', None)

            if role not in allowed_roles:
                return HttpResponseForbidden("You do not have permission to access this page.")

            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator



# def role_required(allowed_roles):
#     """Restrict access based on organization invitation role."""
#
#     def decorator(view_func):
#         @wraps(view_func)
#         def _wrapped_view(request, *args, **kwargs):
#             invitation = OrganizationInvitation.objects.filter(
#                 email=request.user.email,
#                 organization_name_id=getattr(request.user.organization_name, 'id', None),
#                 status=OrganizationInvitation.ACCEPTED
#             ).first()
#
#             # invitation = OrganizationInvitation.objects.filter(
#             #     email=request.user.email, status='accepted'
#             # ).first()
#             if not invitation or invitation.role not in allowed_roles:
#                 return HttpResponseForbidden("You do not have permission to access this page.")
#             return view_func(request, *args, **kwargs)
#
#         return _wrapped_view
#
#     return decorator


# -------------------- Service Function --------------------

# -------------------- Service Function --------------------

def get_user_permissions(user):
    """
    Return a dictionary of permissions based on accepted invitation role.
    Fallback to user.role if no accepted invitation exists.
    """
    org = getattr(user, 'organization_name', None)
    org_id = org.id if org else None

    invitation = OrganizationInvitation.objects.filter(
        email=user.email,
        organization_name_id=org_id,
        status=OrganizationInvitation.ACCEPTED
    ).first()

    permissions = {
        # Vision
        'vision_view': False,
        'vision_create': False,
        'vision_edit': False,
        'vision_delete': False,

        # Mission
        'mission_view': False,
        'mission_create': False,
        'mission_edit': False,
        'mission_delete': False,

        # Organizational Profile
        'organization_view': False,
        'organization_edit': False,

        # Invitations
        'invitation_view': False,
        'invitation_send': False,
        'invitation_delete': False,
    }

    # Determine role: invitation role or user role fallback
    role = invitation.role if invitation else getattr(user, 'role', None)

    if role == 'editor':
        permissions.update({
            'vision_view': True,
            'vision_create': True,
            'vision_edit': True,
            'vision_delete': True,

            'mission_view': True,
            'mission_create': True,
            'mission_edit': True,
            'mission_delete': True,

            'organization_view': True,
            'organization_edit': True,

            'invitation_view': True,
            'invitation_send': True,
            'invitation_delete': True,
        })
    elif role == 'viewer':
        permissions.update({
            'vision_view': True,
            'mission_view': True,
            'organization_view': True,
        })

    return permissions



#
# def get_user_permissions(user):
#     """
#     Return a dictionary of permissions based on the user's accepted invitation role.
#     Considers Vision, Mission, OrganizationalProfile, and Invitations.
#     """
#     # Get user's organization ID safely
#     org = getattr(user, 'organization_name', None)
#     org_id = org.id if org else None
#
#     # Check accepted invitation for this user in their organization
#     invitation = OrganizationInvitation.objects.filter(
#         email=user.email,
#         organization_name_id=org_id,
#         status=OrganizationInvitation.ACCEPTED
#     ).first()
#
#     # Default permissions
#     permissions = {
#         # Vision
#         'vision_view': False,
#         'vision_create': False,
#         'vision_edit': False,
#         'vision_delete': False,
#
#         # Mission
#         'mission_view': False,
#         'mission_create': False,
#         'mission_edit': False,
#         'mission_delete': False,
#
#         # Organizational Profile
#         'organization_view': False,
#         'organization_edit': False,
#
#         # Invitations
#         'invitation_view': False,
#         'invitation_send': False,
#         'invitation_delete': False,
#     }
#
#     if invitation:
#         if invitation.role == 'editor':
#             permissions.update({
#                 'vision_view': True,
#                 'vision_create': True,
#                 'vision_edit': True,
#                 'vision_delete': True,
#
#                 'mission_view': True,
#                 'mission_create': True,
#                 'mission_edit': True,
#                 'mission_delete': True,
#
#                 'organization_view': True,
#                 'organization_edit': True,
#
#                 'invitation_view': True,
#                 'invitation_send': True,
#                 'invitation_delete': True,
#             })
#         elif invitation.role == 'viewer':
#             permissions.update({
#                 'vision_view': True,
#                 'mission_view': True,
#                 'organization_view': True,
#             })
#
#     return permissions
#
