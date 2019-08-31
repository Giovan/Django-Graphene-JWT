# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from django.core.management import call_command


def load_my_initial_data(apps, schema_editor):
    call_command("loaddata", "movies.json")


class Migration(migrations.Migration):
    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_my_initial_data),
    ]