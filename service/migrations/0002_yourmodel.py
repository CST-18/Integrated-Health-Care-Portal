# Generated by Django 3.2.23 on 2023-12-20 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='YourModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dropdown_value', models.CharField(max_length=255)),
            ],
        ),
    ]
