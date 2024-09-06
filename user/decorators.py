from django.core.exceptions import PermissionDenied

def role_required(*role_names):
    """
    Decorator to check if a user has one of the specified roles.
    """
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and any(request.user.groups.filter(name=role_name).exists() for role_name in role_names):
                return view_func(request, *args, **kwargs)
            else:
                raise PermissionDenied
        return _wrapped_view
    return decorator
