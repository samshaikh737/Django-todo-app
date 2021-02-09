from django.contrib import admin
from .models import TodoData

@admin.register(TodoData)

class TodoAdmin(admin.ModelAdmin):
    list_display = ['id','input_text']
