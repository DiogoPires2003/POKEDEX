from django.apps import AppConfig


class PokedexAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pokedex_app'
    def ready(self):
        import pokedex_app.models
