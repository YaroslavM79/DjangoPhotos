from djangophotos.settings.base import *

#override base settings

SECRET_KEY = '38rvjq%s_p9$_5e_49$$e^o3rof46#6)tzhsm=db4dj$@8_1o%'

try:
    from djangophotos.settings.local import *
except:
    pass


