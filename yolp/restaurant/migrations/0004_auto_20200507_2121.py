# Generated by Django 3.0.5 on 2020-05-07 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_auto_20200507_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='price',
            field=models.CharField(choices=[('$', '$'), ('$$', '$$'), ('$$$', '$$$'), ('$$$$', '$$$$')], default='$', max_length=4, null=True),
        ),
    ]