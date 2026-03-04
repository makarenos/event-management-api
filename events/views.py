from rest_framework import viewsets, permissions, generics
from .models import Event, EventRegistration
from .serializers import EventSerializer, EventRegistrationSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)


class EventRegistrationView(generics.CreateAPIView):
    serializer_class = EventRegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        event_id = self.kwargs['event_id']
        event = Event.objects.get(pk=event_id)

        if EventRegistration.objects.filter(event=event,
                                            user=self.request.user).exists():
            raise ValidationError("Ти вже зареєстрований на цей івент")

        serializer.save(user=self.request.user, event=event)