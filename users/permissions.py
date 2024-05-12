from rest_framework.permissions import BasePermission


class IsActive(BasePermission):
    """Permission for checking user is active"""
    message = "User is not active"

    def has_permission(self, request, view):
        return request.user.is_active == True
