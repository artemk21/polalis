from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

# touched on 2025-05-27T15:29:10.581536Z
# touched on 2025-07-09T21:54:11.531051Z
# touched on 2025-07-09T21:54:18.512961Z
# touched on 2025-07-09T21:54:25.203161Z
# touched on 2025-07-09T21:54:32.755739Z
# touched on 2025-07-09T21:54:49.474955Z
# touched on 2025-07-09T21:55:02.050388Z