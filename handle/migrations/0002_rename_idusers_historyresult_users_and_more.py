# Generated by Django 4.2 on 2023-04-08 04:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handle', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historyresult',
            old_name='idUsers',
            new_name='users',
        ),
        migrations.RenameField(
            model_name='mywords',
            old_name='idUsers',
            new_name='users',
        ),
        migrations.RenameField(
            model_name='mywords',
            old_name='idWord',
            new_name='word',
        ),
        migrations.RenameField(
            model_name='words',
            old_name='idTopic',
            new_name='topic',
        ),
        migrations.AlterField(
            model_name='historyresult',
            name='timeStart',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 8, 11, 12, 26, 58153)),
        ),
    ]