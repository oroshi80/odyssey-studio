from django.contrib import admin
from .models import GitHubRepository

@admin.register(GitHubRepository)
class GitHubRepositoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'path', 'status')  # Fields to display in the admin list view
    search_fields = ('name', 'path')  # Fields to search in the admin
