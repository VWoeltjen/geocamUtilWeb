# __BEGIN_LICENSE__
#Copyright (c) 2015, United States Government, as represented by the 
#Administrator of the National Aeronautics and Space Administration. 
#All rights reserved.
# __END_LICENSE__

from django.conf import settings


def AuthUrlsContextProcessor(request):
    """
    Adds login and logout urls to the context.
    """
    if hasattr(settings, 'LOGIN_DEFAULT_NEXT_URL'):
        # deprecated. we originally chose LOGIN_DEFAULT_NEXT_URL because we did not know about LOGIN_REDIRECT_URL.
        loginSuffix = '?next=' + settings.LOGIN_DEFAULT_NEXT_URL
    elif hasattr(settings, 'LOGIN_REDIRECT_URL'):
        # LOGIN_REDIRECT_URL is the settings field that Django's auth module uses for this purpose
        # https://docs.djangoproject.com/en/dev/ref/settings/
        loginSuffix = '?next=' + settings.LOGIN_REDIRECT_URL
    else:
        loginSuffix = ''

    return {
        'login_url': settings.LOGIN_URL,
        'logout_url': settings.LOGIN_URL,
        'login_url_with_next': settings.LOGIN_URL + loginSuffix
    }
