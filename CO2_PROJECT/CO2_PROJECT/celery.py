import os 
from celery import Celery

# 1. Deve apontar corretamente para o seu settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CO2_PROJECT.settings')

app = Celery('CO2_PROJECT')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()