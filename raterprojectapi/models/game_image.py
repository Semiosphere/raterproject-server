from django.db import models

class Game_Image(models.Model):
    player_id = models.ForeignKey("Player",  on_delete=models.CASCADE)
    game_id = models.ForeignKey("Game",  on_delete=models.CASCADE)
    