# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-01-26 20:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('active_user', '0008_madadjoo_hamyar_letter_title'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='hamyar_madadjoo_meeting',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='hamyar_madadjoo_payment',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='hamyar_system_payment',
            unique_together=set([]),
        ),
        migrations.AlterUniqueTogether(
            name='madadjoo_hamyar_letter',
            unique_together=set([]),
        ),
    ]
