from rest_framework import routers, serializers, viewsets
from .models import Player
class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ["url","player_name","nationality","born","birthplace","height","role","batting_style","bowling_style","teams","total_ing","total_run","total_hun","total_fif","total_bowling_ing","total_wicket","total_economy","total_avg","small_info","photo"]