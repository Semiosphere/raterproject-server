from django.db import models

class Game_Image(models.Model):
    player = models.ForeignKey("Player",  on_delete=models.CASCADE)
    game = models.ForeignKey("Game",  on_delete=models.CASCADE)
    