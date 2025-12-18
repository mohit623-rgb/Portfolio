from django.contrib import admin
from .models import Student

admin.site.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "short_message", "website", "branding", "ecommerce", "seo"]