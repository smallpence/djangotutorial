"app metadata - used for importing"

from django.apps import AppConfig


class PollsConfig(AppConfig):
    "config for polls"
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
