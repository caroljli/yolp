# Generated by Django 3.0.5 on 2020-05-08 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20200508_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='picture',
            field=models.CharField(default=None, max_length=600, null=True),
        ),
    ]
