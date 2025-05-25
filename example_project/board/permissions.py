from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    get - allowany
    others - writer only
    """

    def has_permission(self, request, view):
        # GET, HEAD, OPTIONS allowany
        if request.method in permissions.SAFE_METHODS:
            return True

        # others
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # GET, HEAD, OPTIONS # GET, HEAD, OPTIONS allowany
        if request.method in permissions.SAFE_METHODS:
            return True

        # others
        return obj.author == request.user
