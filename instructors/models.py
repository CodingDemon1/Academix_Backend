from django.db import models


class Instructor(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    id = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
    )
    name = models.TextField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    department = models.TextField()
    email = models.EmailField(unique=True)
    contact_number = models.TextField()
    password = models.CharField(max_length=128, blank=True)
    isAuthorized = models.BooleanField(default=False)

    def __str__(self):
        return self.name
