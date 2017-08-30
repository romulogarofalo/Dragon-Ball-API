# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sagas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nm_character', models.CharField(max_length=100)),
                ('img_character', models.CharField(max_length=500)),
                ('fighting_power', models.IntegerField()),
                ('saga_id', models.ForeignKey(related_name='saga', to='sagas.saga')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='type_character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nm_type_character', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='character',
            name='type_id',
            field=models.ForeignKey(related_name='type_character', to='character.type_character'),
            preserve_default=True,
        ),
    ]
