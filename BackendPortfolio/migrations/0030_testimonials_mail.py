# Generated by Django 4.2.6 on 2023-12-27 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackendPortfolio', '0029_remove_mypic_baniere'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonials',
            name='Mail',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]
