from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Temp_humi(models.Model):
    temp_humi_id=models.AutoField(primary_key=True)
    temp=models.IntegerField(default=0)
    humi=models.IntegerField(default=0)
    date_time=models.DateTimeField('date and time')

    def __int__(self):
        return self.temp_humi_id
