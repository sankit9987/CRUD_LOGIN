from django.contrib import admin
from .models import entry
# Register your models here.
@admin.register(entry)
class Useradmin(admin.ModelAdmin):
    list_display = [
        'id','name','contact'
    ]