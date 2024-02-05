from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdim(admin.ModelAdmin):
  ...
