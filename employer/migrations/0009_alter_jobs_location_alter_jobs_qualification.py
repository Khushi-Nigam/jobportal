# Generated by Django 5.0.4 on 2024-09-02 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0008_remove_post_cpemailaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='location',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='qualification',
            field=models.CharField(max_length=50),
        ),
    ]
