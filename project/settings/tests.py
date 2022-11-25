from tempfile import TemporaryDirectory

from . import *  # noqa

CELERY_TASK_ALWAYS_EAGER = True

INSTALLED_APPS += ("project.geosource.tests.app",)  # NOQA
MEDIA_ROOT = TemporaryDirectory().name
