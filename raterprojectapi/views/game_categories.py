from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from raterprojectapi.models.game_category import Game_Category

class GameCategoryView(ViewSet):
    
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized game_category instance
        """
        serializer = CreateGameCategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
class GameCategorySerializer(serializers.ModelSerializer):
    """JSON serializer for game_categories
    """
    class Meta:
        model = Game_Category
        fields = ('id', 'game', 'category')
        
class CreateGameCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Game_Category
        fields = ['id', 'game', 'category']