# Generated by Django 5.0.4 on 2024-08-05 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobseeker',
            name='profilepic',
            field=models.FileField(default='pic', upload_to=''),
        ),
    ]
