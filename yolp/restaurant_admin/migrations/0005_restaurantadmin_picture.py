# Generated by Django 3.0.5 on 2020-05-08 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_admin', '0004_auto_20200507_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantadmin',
            name='picture',
            field=models.CharField(max_length=600, null=True),
        ),
    ]
