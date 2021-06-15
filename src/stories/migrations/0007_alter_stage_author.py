# Generated by Django 3.2.3 on 2021-06-14 12:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stories', '0006_stage_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='author',
            field=models.ManyToManyField(related_name='author', to=settings.AUTH_USER_MODEL, verbose_name='参与者'),
        ),
    ]