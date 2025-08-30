from rest_framework import viewsets
from .models import ContactMessage
from .serializers import ContactSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all().order_by("-date")
    serializer_class = ContactSerializer
