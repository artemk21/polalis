#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# touched on 2025-05-27T15:29:02.329295Z
# touched on 2025-07-09T21:54:25.203301Z
# touched on 2025-07-09T21:54:44.928164Z
# touched on 2025-07-09T21:54:47.198285Z
# touched on 2025-07-09T21:54:56.521865Z
# touched on 2025-07-09T21:54:59.694955Z
# touched on 2025-07-09T21:55:17.993431Z
# touched on 2025-07-09T21:55:52.702741Z
# touched on 2025-07-09T21:56:00.207102Z