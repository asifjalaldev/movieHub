
from rest_framework import permissions

class CustomReviewUserOrReadOnly(permissions.BasePermission):

    message='admin or read only'

    # def has_permission(self, request, view):
    #     if request.method=='GET':
    #         return request.user.is_authenticated
    #     else:
    #         return request.user.is_staff

    def has_object_permission(self, request, view, obj):
        if request.method=='GET':
            return True
        else: # if post or put request
            # obj mean curent model object which is being updated
            if obj.user == request.user:
                # if model object created by the authenticated user then grant access to the specified view task
                return True
            else: 
                return False
        # return super().has_object_permission(request, view, obj)