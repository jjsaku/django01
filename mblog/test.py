import os, csv, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mblog.settings')
django.setup()

from mysite import models

data = models.Vote.objects.all().order_by('votes')

print(data)