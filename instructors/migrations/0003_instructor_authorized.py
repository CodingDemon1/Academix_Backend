# Generated by Django 4.2.4 on 2023-09-04 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0002_instructor_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='authorized',
            field=models.BooleanField(default=False),
        ),
    ]
