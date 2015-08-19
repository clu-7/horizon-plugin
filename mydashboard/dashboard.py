from django.utils.translation import ugettext_lazy as _

import horizon


class Mydashboard(horizon.Dashboard):
    name = _("My Dashboard")
    slug = "mydashboard"
    panels = ('mypanel',)  # Add your panels here.
    default_panel = 'mypanel'  # Specify the slug of the dashboard's default panel.


horizon.register(Mydashboard)
