from rest_framework import permissions

class IsAdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        admin_permission = bool(request.user and request.user.is_staff)
        if request.method in permissions.SAFE_METHODS:
            return True
        else :
            return admin_permission

class IsContactUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.contact_user == request.user