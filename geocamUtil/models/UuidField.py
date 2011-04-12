# __BEGIN_LICENSE__
# Copyright (C) 2008-2010 United States Government as represented by
# the Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
# __END_LICENSE__

try:
    import uuid
except ImportError:
    uuid = None

from django.db import models

if uuid:
    def makeUuid():
        return str(uuid.uuid4())
else:
    import random
    def makeUuid():
        return '%04x-%02x-%02x-%02x-%06x' % (random.getrandbits(32), random.getrandbits(8),
                                             random.getrandbits(8), random.getrandbits(8),
                                             random.getrandbits(48))

class UuidField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 48)
        kwargs.setdefault('editable', False)
        super(UuidField, self).__init__(self, *args, **kwargs)
        
    def pre_save(self, model_instance, add):
        if add and not getattr(model_instance, self.attname):
            value = makeUuid()
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(UuidField, self).pre_save(model_instance, add)

HAVE_SOUTH = False
try:
    import south
    HAVE_SOUTH = True
except ImportError:
    pass

if HAVE_SOUTH:
    # tell south it can freeze this field without any special nonsense
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^geocamUtil\.models\.UuidField"])
