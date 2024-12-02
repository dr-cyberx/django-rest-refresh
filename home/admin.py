from django.contrib import admin
from .models import Person,Color
from django.apps import apps

# Register your models here. manual process
# admin.site.register(Person)
# admin.site.register(Color)

# Register your models here. Automated process
# Get all models in the current app
models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass  # Skip already registered models
