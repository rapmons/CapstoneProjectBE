# Generated by Django 4.2 on 2023-05-20 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('handle', '0003_remove_historyresult_timestart_historyresult_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='historySearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('idSearch', models.IntegerField(default=0)),
                ('delete', models.BooleanField(default=0)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='handle.users')),
            ],
        ),
    ]
