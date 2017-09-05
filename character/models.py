from django.db import models
from sagas.models import saga
# Create your models here.
class type_character(models.Model):
    nm_type_character = models.CharField(max_length=100, null=False)

class character(models.Model):
    nm_character = models.CharField(max_length=100, null=False)
    img_character = models.CharField(max_length=500, null=False)
    fighting_power = models.CharField(max_length=100, null=False)
    type_id = models.ForeignKey(type_character, related_name='type_character')
    saga_id = models.ForeignKey(saga, related_name="saga")
    

