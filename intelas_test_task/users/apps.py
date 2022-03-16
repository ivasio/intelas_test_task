from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "intelas_test_task.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import intelas_test_task.users.signals  # noqa F401
        except ImportError:
            pass
