# Generated by Django 3.0.5 on 2020-05-07 22:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_auto_20200507_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0002_auto_20200507_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restaurant.Restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='following',
            field=models.ManyToManyField(null=True, to='student.Follow'),
        ),
    ]