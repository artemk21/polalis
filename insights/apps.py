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
# touched on 2025-07-09T21:56:00.206927Z
# touched on 2025-07-09T21:56:02.775830Z
# touched on 2025-07-09T21:56:07.671780Z
# touched on 2025-07-09T21:56:12.463956Z
# touched on 2025-07-09T21:56:16.817684Z
# touched on 2025-07-09T21:56:21.417201Z
# touched on 2025-07-09T21:56:23.844025Z
# touched on 2025-07-09T21:56:49.530517Z
# touched on 2025-07-09T21:56:56.671861Z
# touched on 2025-07-09T21:57:51.557323Z