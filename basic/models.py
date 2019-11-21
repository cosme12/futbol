import random

from django.db import models
from django.contrib.auth.models import AbstractUser
from .extra_data import NAMES

# Create your models here.


class Season(models.Model):
    date = models.DateTimeField(null=True)


class League(models.Model):
    level = models.IntegerField(default=1)
    id_season = models.ForeignKey(Season, null=True, on_delete=models.SET_NULL)
    matches_played = models.IntegerField(default=0)


class Team(models.Model):
    id_league = models.ForeignKey(League, null=True, on_delete=models.SET_NULL)
    name = models.TextField(null=True)
    points = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)
    fans = models.IntegerField(default=0)
    money = models.IntegerField(default=0)
    last_year_place = models.IntegerField(default=0)
    elo = models.IntegerField(default=0)
    last_year_elo = models.IntegerField(default=0)


class CustomUser(AbstractUser):
    team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)
    cheated = models.IntegerField(default=0)
    info_text = models.TextField(null=True)
    accepted_rules = models.IntegerField(default=0)
    licensed = models.IntegerField(default=0)
    welcomed_message = models.IntegerField(default=0)
    sanctions = models.IntegerField(default=0)


class Notification(models.Model):
    id_user = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)
    text = models.TextField(null=True)
    type = models.TextField(null=True)
    date = models.DateTimeField(null=True)


class Player(models.Model):
    id_team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)
    name = models.TextField(null=True)
    surname = models.TextField(null=True)
    position = models.TextField(null=True)
    age = models.IntegerField(default=18)
    freshness = models.IntegerField(default=100)
    games_played_club = models.IntegerField(default=0)
    games_played_total = models.IntegerField(default=0)
    skill_current = models.FloatField(default=0)
    skill_max = models.FloatField(default=0)
    market_value = models.FloatField(default=0)
    salary = models.FloatField(default=0)
    last_improvement = models.DateTimeField(null=True)
    moral = models.FloatField(default=100)

    @staticmethod
    def create_players(n_players):
        names = random.sample(NAMES, n_players)
        for name in names:
            new_item = Player(name=name.capitalize(), surname='Perez', position='D', age=18, )
            new_item.save()


class Formation(models.Model):
    id_team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)
    active = models.IntegerField(default=0)


class FormationSetup(models.Model):
    id_formation = models.ForeignKey(Formation, null=True, on_delete=models.SET_NULL)
    id_player = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL)


class Match(models.Model):
    id_season = models.ForeignKey(Season, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(null=True)
    viewers = models.IntegerField(default=0)
    result = models.TextField(null=True)
    simulated = models.IntegerField(default=0)
    possession_1 = models.IntegerField(default=0)
    possession_2 = models.IntegerField(default=0)
    fouls_1 = models.IntegerField(default=0)
    fouls_2 = models.IntegerField(default=0)
    yellow_card_1 = models.IntegerField(default=0)
    yellow_card_2 = models.IntegerField(default=0)
    red_card_1 = models.IntegerField(default=0)
    red_card_2 = models.IntegerField(default=0)


class MatchAssignment(models.Model):
    id_match = models.ForeignKey(Match, null=True, on_delete=models.SET_NULL)
    id_team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)


class MatchCommentary(models.Model):
    id_match = models.ForeignKey(Match, null=True, on_delete=models.SET_NULL)
    minute = models.IntegerField(default=0)
    commentary = models.TextField(null=True)

