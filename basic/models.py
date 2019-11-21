import random
from datetime import datetime, timedelta

from django.db import models
from django.contrib.auth.models import AbstractUser
from .extra_data import NAMES, SURNAMES, TEAM_NAMES


# Create your models here.


class Season(models.Model):
    date = models.DateTimeField(null=True)

    @staticmethod
    def create_season():
        date = datetime.now() + timedelta(days=1)
        new_season = Season(date=date)
        new_season.save()


class League(models.Model):
    level = models.IntegerField(default=1)
    id_season = models.ForeignKey(Season, null=True, on_delete=models.SET_NULL)
    matches_played = models.IntegerField(default=0)

    @staticmethod
    def create_leagues(levels):
        # levels(list): [1,2,2,2,3,3,3,3,3,3,3,3,3]
        for level in levels:
            new_league = League(level=level)
            new_league.save()


class Team(models.Model):
    id_league = models.ForeignKey(League, null=True, on_delete=models.SET_NULL)
    name = models.TextField()
    points = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)
    fans = models.IntegerField(default=0)
    money = models.IntegerField(default=5000000)
    last_year_place = models.IntegerField(default=0)
    elo = models.IntegerField(default=1200)
    last_year_elo = models.IntegerField(default=0)

    @staticmethod
    def create_teams(n_teams):
        names = random.sample(TEAM_NAMES, n_teams)
        for name in names:
            new_team = Team(name=name)
            new_team.save()

    @staticmethod
    def assign_team_to_league():
        teams_no_league = Team.objects.filter(id_league=None)
        all_leagues = League.objects.filter()
        for team in teams_no_league:
            for league in all_leagues:
                if Team.objects.filter(id_league=league.id).count() < 12:
                    team.id_league = league
                    team.save()
                    break


class CustomUser(AbstractUser):
    id_team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)
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
    name = models.TextField()
    surname = models.TextField(null=True)
    position = models.TextField(null=True)
    age = models.IntegerField(default=18)
    freshness = models.IntegerField(default=100)
    games_played_club = models.IntegerField(default=0)
    games_played_total = models.IntegerField(default=0)
    skill_current = models.FloatField(default=0)
    skill_max = models.FloatField(default=0)
    market_value = models.FloatField(default=0)
    salary = models.FloatField(default=0)  # Cost per day to have this player in your team. Adjust every season
    last_improvement = models.DateTimeField(null=True)
    moral = models.FloatField(default=100)

    @staticmethod
    def create_players(n_players, position):
        # position(str): Arq,Def,Med,Ofen
        names = random.sample(NAMES, n_players)
        surnames = random.sample(SURNAMES, n_players)
        skill_max_list = [round(random.uniform(4, 10), 1) for _ in range(n_players)]
        skill_current_list = [round(random.uniform(1.0, 4), 1) for _ in range(n_players)]

        for name, surname, skill_current, skill_max in zip(names, surnames, skill_current_list, skill_max_list):
            salary = round((2.3**(skill_current/0.8))*455)
            new_player = Player(name=name.capitalize(), surname=surname.capitalize(), position=position,
                                skill_current=skill_current, skill_max=skill_max, salary=salary)
            new_player.save()

    @staticmethod
    def assign_player_to_team():
        players_no_team = Player.objects.filter(id_team=None)
        all_teams = Team.objects.filter()
        for player in players_no_team:
            for team in all_teams:
                if Player.objects.filter(id_team=team.id).count() < 15:
                    player.id_team = team
                    player.save()
                    break


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

