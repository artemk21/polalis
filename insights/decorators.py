from django.http import HttpResponseForbidden

def role_required(required_role):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if hasattr(request.user, 'userprofile') and request.user.userprofile.role == required_role:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("⛔ You are not authorized to access this page.")
        return _wrapped_view
    return decorator

# touched on 2025-05-27T15:28:56.617211Z
# touched on 2025-05-27T15:29:05.129847Z
# touched on 2025-07-09T21:54:08.767169Z
# touched on 2025-07-09T21:54:14.003247Z
# touched on 2025-07-09T21:54:20.797786Z
# touched on 2025-07-09T21:54:23.046022Z
# touched on 2025-07-09T21:54:27.831562Z
# touched on 2025-07-09T21:54:30.475444Z
# touched on 2025-07-09T21:54:51.632240Z
# touched on 2025-07-09T21:55:31.783664Z
# touched on 2025-07-09T21:55:44.117045Z
# touched on 2025-07-09T21:55:57.335549Z
# touched on 2025-07-09T21:56:12.465644Z
# touched on 2025-07-09T21:56:16.818009Z
# touched on 2025-07-09T21:57:34.706811Z