# Generated by Django 3.2.3 on 2021-05-29 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default='', help_text='正文为MarkDown格式', verbose_name='正文'),
        ),
    ]