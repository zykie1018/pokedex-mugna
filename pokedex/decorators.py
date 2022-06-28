from functools import wraps
from django.http import HttpResponse
from django.shortcuts import redirect
from functools import wraps


def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper_func(request, *args, **kwargs):
            if request.user.groups.filter(name__in=allowed_roles).exists():
                return view_func(request, *args, **kwargs)

            else:
                return HttpResponse("You are not authorized to view this page!")

        return wrapper_func

    return decorator
