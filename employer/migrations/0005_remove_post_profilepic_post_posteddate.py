# Generated by Django 5.0.4 on 2024-08-14 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0004_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='profilepic',
        ),
        migrations.AddField(
            model_name='post',
            name='posteddate',
            field=models.CharField(default='', max_length=30),
        ),
    ]
