from django.apps import AppConfig


class InsightsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'insights'

    def ready(self):
        import insights.signals
# touched on 2025-05-27T15:28:53.859328Z
# touched on 2025-07-09T21:54:40.534466Z
# touched on 2025-07-09T21:54:42.866064Z
# touched on 2025-07-09T21:54:44.928012Z
# touched on 2025-07-09T21:54:47.197735Z
# touched on 2025-07-09T21:54:51.631964Z
# touched on 2025-07-09T21:54:53.929452Z
# touched on 2025-07-09T21:55:10.839941Z
# touched on 2025-07-09T21:55:17.993684Z
# touched on 2025-07-09T21:55:48.180432Z