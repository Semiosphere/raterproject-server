from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from raterprojectapi.models import Review, Player
from django.contrib.auth.models import User

class ReviewView(ViewSet):
    def retrieve(self, request,pk):
        
        review = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
        
    def list(self, request):
        
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized game instance
        """
        user = User.objects.get(auth_token=request.data["player"])
        player = Player.objects.get(user=request.auth.user)
        serializer = CreateReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(player=player)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for reviews
    """
    class Meta:
        model = Review
        fields = ('id', 'game', 'player', 'review')
        
class CreateReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for reviews
    """
    class Meta:
        model = Review
        fields = ('id', 'game', 'review')