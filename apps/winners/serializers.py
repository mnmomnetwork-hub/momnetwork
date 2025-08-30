from rest_framework import serializers
from .models import WeeklyWinner

class WinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyWinner
        fields = "__all__"
