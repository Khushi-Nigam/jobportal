# Generated by Django 5.0.4 on 2024-08-21 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0006_alter_post_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cpemailaddress',
            field=models.EmailField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='post',
            name='cpname',
            field=models.TextField(default='', max_length=300),
        ),
    ]
