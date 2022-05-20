from django.db import models


class Review(models.Model):
    
    player = models.ForeignKey("Player",  on_delete=models.CASCADE)
    game = models.ForeignKey("Game",  on_delete=models.CASCADE, related_name="reviewed")
    review = models.CharField(max_length=500)