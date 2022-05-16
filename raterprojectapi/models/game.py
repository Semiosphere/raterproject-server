from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    designer = models.CharField(max_length=50)
    release_year = models.IntegerField()
    number_of_players = models.CharField(max_length=50)
    est_playtime = models.CharField(max_length=50)
    rec_age = models.CharField(max_length=50)