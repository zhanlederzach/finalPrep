# Generated by Django 2.2 on 2019-04-30 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiOld', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_at',
        ),
    ]
