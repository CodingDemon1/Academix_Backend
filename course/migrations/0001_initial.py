# Generated by Django 4.2.4 on 2023-08-31 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('instructors', '0002_instructor_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.TextField()),
                ('course_name', models.TextField()),
                ('department', models.TextField()),
                ('credits', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='instructors.instructor')),
            ],
        ),
    ]