from rest_framework.permissions import SAFE_METHODS, BasePermission

from .models import UserRoles


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.author


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.role == UserRoles.MODERATOR

    def has_object_permission(self, request, view, obj):
        user = request.user
        return user.is_authenticated and user.role == UserRoles.MODERATOR


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.role == UserRoles.ADMIN

    def has_object_permission(self, request, view, obj):
        user = request.user
        return user.is_authenticated and user.role == UserRoles.ADMIN
