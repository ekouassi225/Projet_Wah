# Generated by Django 4.2.6 on 2023-12-28 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackendPortfolio', '0032_alter_testimonials_datepub'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fact',
            old_name='visite',
            new_name='projet',
        ),
        migrations.AddField(
            model_name='fact',
            name='collab',
            field=models.IntegerField(default=False),
        ),
    ]
