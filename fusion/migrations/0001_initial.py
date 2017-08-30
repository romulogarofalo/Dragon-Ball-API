# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='fusion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nm_character_fusion', models.CharField(max_length=100)),
                ('character1_id', models.ForeignKey(related_name='character1_id', to='character.character')),
                ('character2_id', models.ForeignKey(related_name='character2_id', to='character.character')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='type_fusion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nm_type_fusion', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='fusion',
            name='type_fusion_id',
            field=models.ForeignKey(related_name='type_fusion', to='fusion.type_fusion'),
            preserve_default=True,
        ),
    ]
