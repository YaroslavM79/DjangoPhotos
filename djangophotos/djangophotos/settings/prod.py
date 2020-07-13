from djangophotos.settings.base import *

#override base settings

DEBUG = False
ALLOWED_HOSTS = ['*']


try:
    from djangophotos.settings.local import *
except:
    pass
