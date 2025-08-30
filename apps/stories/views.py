from rest_framework import viewsets
from .models import Story
from .serializers import StorySerializer

class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all().order_by("-created_at")
    serializer_class = StorySerializer

    def get_queryset(self):
        if self.request.method == "GET":
            return Story.objects.filter(status="approved", share_publicly=True).order_by("-created_at")
        return super().get_queryset()
