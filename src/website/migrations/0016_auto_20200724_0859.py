# Generated by Django 3.0.7 on 2020-07-24 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_remove_countnumber_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500, verbose_name='Question')),
                ('answer', models.CharField(max_length=500, verbose_name='Answer')),
                ('position', models.IntegerField(default='0')),
            ],
            options={
                'verbose_name': 'Faq',
                'ordering': ['position'],
            },
        ),
        migrations.AlterModelOptions(
            name='countnumber',
            options={'ordering': ['position'], 'verbose_name': 'Count number'},
        ),
    ]
