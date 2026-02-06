from django.db import models

class Portfolio(models.Model):
    CATEGORY_CHOICES = [
        ('design', 'Graphic Design'),
        ('printing', 'Printing'),
        ('branding', 'Branding'),
        ('apparel', 'Apparel'),
    ]

    title = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    date = models.DateField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()

    image = models.ImageField(upload_to='portfolio/')  # uploads from device
    tags = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.title
