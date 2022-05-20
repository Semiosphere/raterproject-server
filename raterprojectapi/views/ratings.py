from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from raterprojectapi.models import Rating

class RatingView(ViewSet):
    def retrieve(self, request,pk):
        
        rating = Rating.objects.get(pk=pk)
        serializer = RatingSerializer(rating)
        return Response(serializer.data)
        
    def list(self, request):
        
        rating = Rating.objects.all()
        serializer = RatingSerializer(rating, many=True)
        return Response(serializer.data)
    
class RatingSerializer(serializers.ModelSerializer):
    """JSON serializer for ratings
    """
    class Meta:
        model = Rating
        fields = ('id', 'rating')