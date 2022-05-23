from django.apps import AppConfig


class BaseAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_app'

    def ready(self):
        from base_app import updater
        updater.start()
