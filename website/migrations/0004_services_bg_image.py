# Generated by Django 5.0.6 on 2024-05-23 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_whoweare'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='bg_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/service/'),
        ),
    ]