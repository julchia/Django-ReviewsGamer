from django.contrib import admin
from .models import Reviews

# Register your models here.

def aprobar(modeladmin, request, queryset):
    queryset.update(status='Aprobado')

def reprobar(modeladmin, request, queryset):
    queryset.update(status='No aprobado')

class ReviewsAdmin(admin.ModelAdmin):
    readonly_fields = ['created']
    list_display = ['game_name', 'genre', 'plataform', 'created', 'status']
    ordering = ['created']
    list_filter = ('created', 'genre', 'plataform', 'release_year',)
    actions = [aprobar, reprobar]

admin.site.register(Reviews, ReviewsAdmin)

