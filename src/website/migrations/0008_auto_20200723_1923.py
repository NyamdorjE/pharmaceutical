# Generated by Django 3.0.7 on 2020-07-23 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20200723_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to='media/icon'),
        ),
    ]
