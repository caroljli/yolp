# Generated by Django 3.0.5 on 2020-05-07 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20200507_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='picture',
            field=models.CharField(max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='picture',
            field=models.CharField(max_length=600, null=True),
        ),
    ]