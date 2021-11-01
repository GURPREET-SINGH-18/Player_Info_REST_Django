from django.shortcuts import render
from rest_framework import routers, viewsets
from .models import Player
from .serializer import PlayerSerializer
import requests
# Create your views here.
class PlayerViewset(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer