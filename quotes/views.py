# quotes/views.py
from rest_framework import generics
from .models import QuoteRequest
from .serializers import QuoteRequestSerializer
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings


class QuoteCreateView(generics.CreateAPIView):
    serializer_class = QuoteRequestSerializer

    def perform_create(self, serializer):
        quote = serializer.save()

        # Send email notification
        subject = f"New Quote Request from {quote.full_name}"
        message = f"""
        Name: {quote.full_name}
        Email: {quote.email}
        Phone: {quote.phone}
        Company: {quote.company}
        Service Type: {quote.service_type}
        Project Type: {quote.project_type}
        Budget: {quote.budget}
        Deadline: {quote.deadline}
        Message: {quote.message}
        Heard About Us: {quote.hear_about_us}
        """
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_EMAIL],
            fail_silently=False,
        )
