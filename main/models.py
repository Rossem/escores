from django.db import models

# Create your models here.

class Region(models.Model):
    region = models.CharField(max_length=5)

    def __unicode__(self):
        return self.region

class Game(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    def get_game(self):
        return self.name

class Position(models.Model):
    game = models.ForeignKey(Game)
    pass

class LoLPosition(Position):
    position = models.CharField(max_length=10)

    def __unicode__(self):
        return self.position

class League(models.Model):
    league_name = models.CharField(max_length=50)
    league_abr = models.CharField(max_length=10, verbose_name="League Abbreviation")
    num_of_teams = models.IntegerField(default=0)
    region  = models.ForeignKey(Region, related_name = "leagues")
    game = models.ForeignKey(Game, related_name="leagues")

    def __unicode__(self):
        return self.league_abr

class Team(models.Model):
    team_name = models.CharField(max_length=20)
    team_name_abr = models.CharField(max_length=4)
    league = models.ForeignKey(League, related_name="teams")
    game = models.ForeignKey(Game, related_name="teams")


    def __unicode__(self):
        return self.team_name_abr



class Player(models.Model):
    name = models.CharField(max_length=16)
    full_name = models.CharField(max_length=50)
    position = models.ForeignKey(LoLPosition)
    team = models.ForeignKey(Team)
    game = models.ForeignKey(Game)

    free_agent = models.BooleanField(default=True)

    if game == "league of legends":
        position = models.ForeignKey(LeaguePosition)

    else:
        position = models.ForeignKey(Position)

    def __unicode__(self):
        return self.name


class Stats(models.Model):
    team = models.ForeignKey(Team, related_name="stats")
    league = models.ForeignKey(League)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    #games_played = int(wins) + int(losses) + int(draws)

    def __unicode__(self):
        return "Wins: " + str(self.wins) + " Losses: " + str(self.losses) + "Draws: " + str(self.draws)

    class Meta:
        verbose_name_plural = "Stats"

class Match(models.Model): 
    league = models.ForeignKey(League)
    team1 = models.ForeignKey(Team, related_name="team1")
    team2 = models.ForeignKey(Team, related_name="team2")

    def __unicode__(self):
        return "Team 1: " + self.team1.team_name_abr + " Team2: " + self.team1.team_name_abr

    class Meta:
        verbose_name_plural = "Maches"


class News(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    region = models.ForeignKey(Region, related_name = "news_stories")

    def __unicode__(self):
        return self.title + ": " + self.body

    class Meta:
        verbose_name_plural = "News"


