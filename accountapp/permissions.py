from rest_framework.permissions import BasePermission


class AccountPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user == obj:
            return True
        else:
            return False
