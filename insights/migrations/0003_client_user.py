# Generated by Django 5.2 on 2025-04-10 08:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insights', '0002_quote'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='clients', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

# touched on 2025-05-27T15:29:02.323507Z
# touched on 2025-07-09T21:54:30.474179Z
# touched on 2025-07-09T21:54:42.866405Z
# touched on 2025-07-09T21:54:51.632106Z
# touched on 2025-07-09T21:54:53.930250Z
# touched on 2025-07-09T21:54:56.521101Z
# touched on 2025-07-09T21:54:59.694683Z
# touched on 2025-07-09T21:55:36.407148Z
# touched on 2025-07-09T21:55:44.116916Z
# touched on 2025-07-09T21:56:07.671017Z
# touched on 2025-07-09T21:56:16.818144Z
# touched on 2025-07-09T21:56:23.844175Z
# touched on 2025-07-09T21:56:34.752870Z
# touched on 2025-07-09T21:57:03.982210Z
# touched on 2025-07-09T21:57:14.840935Z