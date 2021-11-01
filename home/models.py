from django.db import models
ROLE_CHOICES = (
    ('batsmen','Batsmen'),
    ('bowler', 'Bowler'),
    ('batting_all_rounder','Batting_all_rounder'),
    ('bowling_all_rounder','bowling_all_rounder'),
    ('wk_Batsmen','WK_Batsmen')
)
# Create your models here.
class Player(models.Model):
    player_name=models.CharField(max_length=40,unique=True)
    nationality=models.CharField(max_length=40)
    born=models.CharField(max_length=40)
    birthplace=models.CharField(max_length=40)
    height=models.CharField(max_length=20)
    role=models.CharField(max_length=40,choices=ROLE_CHOICES)
    batting_style=models.CharField(max_length=40)
    bowling_style=models.CharField(max_length=40)
    teams=models.TextField(max_length=1000)
    total_ing=models.IntegerField()
    total_run=models.IntegerField()
    total_avg=models.FloatField()
    total_hun=models.IntegerField()
    total_fif=models.IntegerField()
    total_bowling_ing=models.IntegerField()
    total_wicket=models.IntegerField()
    total_economy=models.FloatField()
    total_avg=models.FloatField()
    small_info=models.TextField(max_length=1000)
    photo=models.ImageField(upload_to='pic')
    
    def __str__(self):
        return self.player_name