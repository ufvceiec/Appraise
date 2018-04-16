# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-14 02:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EvalData', '0031_taskagenda_strategy'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskagenda',
            name='task_type',
            field=models.CharField(blank=True, choices=[('DA', 'Direct Assessment'), ('MM', 'Multimodal Assessment')], max_length=2, verbose_name='Task type'),
        ),
    ]