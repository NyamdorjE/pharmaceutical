# Generated by Django 3.0.7 on 2020-08-03 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_auto_20200722_0942'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='poll',
            options={'ordering': ['question'], 'verbose_name': 'Poll', 'verbose_name_plural': 'Polls'},
        ),
    ]
