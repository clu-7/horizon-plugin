from django.utils.translation import ugettext_lazy as _

import horizon
from mydashboard import dashboard

class Mypanel(horizon.Panel):
    name = _("My Fruits")
    slug = "mypanel"


dashboard.Mydashboard.register(Mypanel)
