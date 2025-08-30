from rest_framework import viewsets
from .models import WeeklyWinner
from .serializers import WinnerSerializer

class WinnerViewSet(viewsets.ModelViewSet):
    queryset = WeeklyWinner.objects.all().order_by("-date")
    serializer_class = WinnerSerializer
