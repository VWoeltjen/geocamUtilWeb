# __BEGIN_LICENSE__
#Copyright (c) 2015, United States Government, as represented by the 
#Administrator of the National Aeronautics and Space Administration. 
#All rights reserved.
# __END_LICENSE__

from geocamUtil.middleware.security import requestIsSecure
from django.conf import settings


def getAccountWidget(request):
    if request.user.is_authenticated():
        accountWidget = ('<a href="%(SCRIPT_NAME)saccounts/profile">%(username)s</a>&nbsp;<a href="%(SCRIPT_NAME)saccounts/logout/">Logout</a>'
                         % dict(SCRIPT_NAME=settings.SCRIPT_NAME, username=request.user.username))
    else:
        path = request.get_full_path()
        if requestIsSecure(request):
            path += '?protocol=http'  # redirect back to http after login

        accountWidget = ('<div id="accountwidget"><a id="login_button" href="%(SCRIPT_NAME)saccounts/login?next=%(path)s">Login</a> | <a id="join_button" href="%(SCRIPT_NAME)saccounts/register">Join</a></div>'
                         % dict(path=path,
                                SCRIPT_NAME=settings.SCRIPT_NAME,
                                username=request.user.username))

    return accountWidget
