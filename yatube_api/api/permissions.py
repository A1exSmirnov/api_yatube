from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_anonymous and (
            request.method not in permissions.SAFE_METHODS
        ):
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.is_anonymous and (
            request.method not in permissions.SAFE_METHODS
        ):
            return False
        return obj.author == request.user