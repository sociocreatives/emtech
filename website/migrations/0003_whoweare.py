# Generated by Django 5.0.6 on 2024-05-19 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_clients_quickfacts_serviceintro_services'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhoWeAre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Who We Are',
            },
        ),
    ]
