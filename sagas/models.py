from django.db import models

class saga(models.Model):
    nm_saga = models.CharField(max_length=100, null=False)
    ds_saga = models.CharField(max_length=1500, null=False)
    img_saga = models.CharField(max_length=1500, null=False)
