from rest_framework import permissions

class IsSuperuserOrIsSelf(permissions.BasePermission):
    """ Check if a user is logged in as superuser or is the self user"""
    
    def has_object_permission(self, request, view, obj):
        """Check the user is trying to changes its own password"""
        if(request.user.is_superuser):
            return True
        return obj.id == request.user.id