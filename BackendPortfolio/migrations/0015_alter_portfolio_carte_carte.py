# Generated by Django 4.2.6 on 2023-12-06 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackendPortfolio', '0014_audio_fact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio_carte',
            name='Carte',
            field=models.ImageField(default=None, upload_to='media_cdn'),
        ),
    ]
