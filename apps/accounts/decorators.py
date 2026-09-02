from functools import wraps

from django.http import HttpResponseForbidden


def role_required(*allowed_roles):

    def decorator(view_func):

        @wraps(view_func)
        def wrapper(request, *args, **kwargs):

            if not request.user.is_authenticated:
                return HttpResponseForbidden(
                    "Authentication required."
                )

            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)

            if request.user.role not in allowed_roles:
                return HttpResponseForbidden(
                    "You do not have permission to access this page."
                )

            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator