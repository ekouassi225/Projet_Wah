# Generated by Django 4.2.6 on 2023-12-26 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackendPortfolio', '0024_justme_lastdiploma_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio_carte',
            name='Carte_suplementaire',
            field=models.ImageField(default=None, upload_to='Backend\\media\\media_cdn'),
        ),
    ]
