# Generated by Django 5.0.4 on 2024-07-21 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jsapp', '0002_response'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appliedjobs',
            name='id',
        ),
        migrations.AlterField(
            model_name='appliedjobs',
            name='jobtitle',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
