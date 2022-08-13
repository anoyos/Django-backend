from rest_framework import permissions

class TokenPermission(permissions.BasePermission):
    """
    Permission class to check that a user can update his own resource only
    """
    def has_permission(self, request, view):
        return True if request.user.id else False