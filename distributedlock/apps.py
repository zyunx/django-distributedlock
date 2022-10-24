from django.apps import AppConfig

if django.VERSION[0] >= 3:
    from django.utils.translation import gettext_lazy as _
else:
    from django.utils.translation import ugettext_lazy as _

class DistributedLockAppConfig(AppConfig):
    name = 'distributedlock'
    verbose_name = _("Distributed Lock")

