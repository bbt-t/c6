from rest_framework.permissions import BasePermission


class IsVerify(BasePermission):
    """
    User must be verified.
    """

    def has_object_permission(self, request, view, obj):
        return request.user.is_verified
