# Generated by Django 5.0.4 on 2024-06-25 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newstext', models.TextField()),
                ('newsdate', models.CharField(max_length=30)),
            ],
        ),
    ]
