import os

from celery import Celery


# let Celery know how to find Django project
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
app = Celery("main")
# this prevent crushes with other Django settings
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()  # tells celery to look for celery tasks
