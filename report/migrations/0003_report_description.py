# Generated by Django 3.1.7 on 2021-03-16 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_auto_20210316_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
