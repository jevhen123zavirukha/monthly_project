# Generated by Django 5.1 on 2024-09-10 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_delete_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technicians',
            name='photo',
            field=models.ImageField(upload_to='technicians'),
        ),
    ]