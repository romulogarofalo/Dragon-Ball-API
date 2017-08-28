from django.db import models
from character.models import character

class type_fusion(models.Model):
    nm_type_fusion = models.CharField(max_length=100, null=False)

class fusion(models.Model):
    type_fusion_id = models.ForeignKey(type_fusion, related_name='type_fusion')
    character1_id = models.ForeignKey(character, related_name='character1_id')
    character2_id = models.ForeignKey(character, related_name='character2_id')
    nm_character_fusion = models.CharField(max_length=100, null=False)
# Create your models here.
