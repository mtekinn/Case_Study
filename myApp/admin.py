from django.contrib import admin

# Register your models here.
from .models import Notes

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')

admin.site.register(Notes, NotesAdmin)