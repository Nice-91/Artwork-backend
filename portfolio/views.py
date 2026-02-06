# portfolio/views.py
from rest_framework import generics
from .models import Portfolio
from .serializers import PortfolioSerializer


class PortfolioListView(generics.ListAPIView):
    serializer_class = PortfolioSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        if category and category != 'all':
            return Portfolio.objects.filter(category=category)
        return Portfolio.objects.all()
