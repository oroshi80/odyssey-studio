from django.db import models

# Create your models here.
class GitHubRepository(models.Model):
    name = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'repo'  # Specify the existing table name if it differs from the model name
        app_label = 'github_api' # Ensure this matches your app name

    def __str__(self):
        return self.name
