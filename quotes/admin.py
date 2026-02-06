from django.contrib import admin
from .models import QuoteRequest


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'email',
        'service_type',
        'project_type',
        'budget',
        'created_at',
    )
