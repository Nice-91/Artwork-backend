# portfolio/admin.py
from django.contrib import admin
from .models import Portfolio

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'category', 'date')
    list_filter = ('category',)
    search_fields = ('title', 'client')

