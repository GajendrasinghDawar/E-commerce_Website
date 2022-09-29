import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'desi_bazar_project.settings')

app = Celery('desi_bazar_project')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# import os
# from celery import Celery

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'desi_bazar_project.settings')
# app = Celery('desi_bazar_project')

# app.config_from_object('django.conf:settings', namespace='CELERY')

# app.autodiscover_tasks()
