# Generated by Django 4.2.6 on 2024-01-18 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackendPortfolio', '0039_portfolio_carte_message_alter_exp_pro_year_end_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exp_pro',
            name='Year_end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='formation',
            name='Year_end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='portfolio_carte',
            name='Message',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='portfolio_carte',
            name='Url',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
