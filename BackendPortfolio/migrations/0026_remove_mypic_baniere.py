# Generated by Django 4.2.6 on 2023-12-26 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BackendPortfolio', '0025_portfolio_carte_carte_suplementaire'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mypic',
            name='baniere',
        ),
    ]
