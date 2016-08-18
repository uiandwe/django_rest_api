__author__ = 'uiandwe'

from functools import wraps

from . import utils


def check_draft(view_func):
    @wraps(view_func)
    def new_view_func(request, *args, **kwargs):
        print("pass decorators")
        print(request, args, kwargs)

        response = view_func(request, *args, **kwargs)

        return response

    return new_view_func