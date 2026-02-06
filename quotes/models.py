from django.db import models


class QuoteRequest(models.Model):
    SERVICE_CHOICES = [
        ('design', 'Graphic Design'),
        ('printing', 'Printing Services'),
        ('branding', 'Branding & Identity'),
        ('apparel', 'Apparel Printing'),
        ('signage', 'Signage & Banners'),
        ('multiple', 'Multiple Services'),
    ]

    PROJECT_CHOICES = [
        ('logo', 'Logo Design'),
        ('business-cards', 'Business Cards'),
        ('brochures', 'Brochures/Flyers'),
        ('banners', 'Banners/Posters'),
        ('tshirts', 'T-Shirts/Apparel'),
        ('vehicle', 'Vehicle Branding'),
        ('packaging', 'Packaging Design'),
        ('website', 'Website Graphics'),
        ('other', 'Other'),
    ]

    BUDGET_CHOICES = [
        ('under-100k', 'Under 100,000 RWF'),
        ('100k-250k', '100,000 - 250,000 RWF'),
        ('250k-500k', '250,000 - 500,000 RWF'),
        ('500k-1m', '500,000 - 1,000,000 RWF'),
        ('over-1m', 'Over 1,000,000 RWF'),
        ('flexible', 'Flexible/Not Sure'),
    ]

    HEAR_ABOUT_US_CHOICES = [
        ('google', 'Google Search'),
        ('social-media', 'Social Media'),
        ('friend', 'Friend/Referral'),
        ('previous-client', 'Previous Client'),
        ('advertisement', 'Advertisement'),
        ('other', 'Other'),
    ]

    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    company = models.CharField(max_length=255, blank=True, null=True)

    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    project_type = models.CharField(max_length=50, choices=PROJECT_CHOICES)
    budget = models.CharField(max_length=50, choices=BUDGET_CHOICES)
    hear_about_us = models.CharField(
        max_length=50,
        choices=HEAR_ABOUT_US_CHOICES,
        blank=True,
        null=True
    )

    deadline = models.DateField(blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
