from django.contrib import admin
from .models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "message", "created_at", "read")  # Adjust fields based on your model
    search_fields = ("name", "email")
    list_filter = ("created_at",)
    ordering = ("-created_at",)