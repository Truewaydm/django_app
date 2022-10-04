from django.apps import AppConfig


# Config my application
# verbose_name = "All news" view in Django admin panel
class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'
    verbose_name = "All news"
