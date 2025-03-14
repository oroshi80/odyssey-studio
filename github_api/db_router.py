# github_api/db_router.py

class GitHubRouter:
       """
       A router to control all database operations on models in the
       github_api application.
       """

       def db_for_read(self, model, **hints):
           """
           Attempts to read github_api models go to github_api.
           """
           if model._meta.app_label == 'github_api':
               return 'github'
           return None

       def db_for_write(self, model, **hints):
           """
           Attempts to write github_api models go to github_api.
           """
           if model._meta.app_label == 'github_api':
               return 'github'
           return None

       def allow_relation(self, obj1, obj2, **hints):
           """
           Allow relations if a model in the github_api app is involved.
           """
           if obj1._meta.app_label == 'github_api' or obj2._meta.app_label == 'github_api':
               return True
           return None

       def allow_migrate(self, db, app_label, model_name=None, **hints):
           """
           Ensure that the github_api app only appears in the
           'github' database.
           """
           if app_label == 'github_api':
               return db == 'github'
           return None