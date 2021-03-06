# Generated by Django 3.0.5 on 2020-05-08 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_restaurant_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='categories', to='restaurant.Category'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.Location'),
        ),
    ]
