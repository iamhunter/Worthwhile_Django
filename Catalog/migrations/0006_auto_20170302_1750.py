# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-02 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0005_auto_20170302_0404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='CourseArt',
            field=models.ImageField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='course',
            name='Duration',
            field=models.CharField(choices=[('8', '8'), ('2', '2')], default='2', max_length=1),
        ),
    ]
