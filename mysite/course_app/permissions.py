from rest_framework import permissions

class CheckOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'teacher':
            return True
        return False

class CheckUserReview(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.user_role == 'student':
            return True
        return False

class CheckCourseOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.teacher == request.user:
            return True
        return False