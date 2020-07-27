# Generated by Django 3.0.7 on 2020-07-23 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20200723_1900'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.FileField(upload_to='media/icon')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=50)),
                ('position', models.IntegerField(default='0')),
            ],
            options={
                'verbose_name': 'Mission',
                'ordering': ['position'],
            },
        ),
    ]
