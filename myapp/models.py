from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    message = models.TextField(blank=True)

    website = models.BooleanField(default=False)
    branding = models.BooleanField(default=False)
    ecommerce = models.BooleanField(default=False)
    seo = models.BooleanField(default=False)

    def __str__(self):
        return self.name
