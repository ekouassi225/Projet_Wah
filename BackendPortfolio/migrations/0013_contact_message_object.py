# Generated by Django 4.2.6 on 2023-12-06 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackendPortfolio', '0012_justme_me'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_message',
            name='Object',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
