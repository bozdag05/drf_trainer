from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)


class IsAuthorAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == permissions.SAFE_METHODS:
            return True

        return obj.user == request.user or bool(request.user and request.user.is_staff)