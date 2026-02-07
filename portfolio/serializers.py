from rest_framework import serializers
from .models import Portfolio


class PortfolioSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Portfolio
        fields = '__all__'

    def get_image(self, obj):
        
        if obj.image:
            return obj.image.url
        return None
