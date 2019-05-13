from django.apps import AppConfig


class InsightsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'insights'

    def ready(self):
        import insights.signals
# touched on 2025-05-27T15:28:53.859328Z
# touched on 2025-07-09T21:54:40.534466Z
# touched on 2025-07-09T21:54:42.866064Z