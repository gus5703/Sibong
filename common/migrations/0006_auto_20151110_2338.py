# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_auto_20151110_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='havestock',
            name='mystock',
            field=models.ForeignKey(to='common.Stock'),
        ),
    ]
