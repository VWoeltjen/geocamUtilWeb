# __BEGIN_LICENSE__
#Copyright (c) 2015, United States Government, as represented by the 
#Administrator of the National Aeronautics and Space Administration. 
#All rights reserved.
# __END_LICENSE__

import time
import rfc822

import django.views.static


def staticServeWithExpires(request, path, document_root=None, show_indexes=False,
                           expireSeconds=365 * 24 * 60 * 60):
    response = django.views.static.serve(request, path, document_root, show_indexes)
    response['Expires'] = rfc822.formatdate(time.time() + expireSeconds)
    return response
