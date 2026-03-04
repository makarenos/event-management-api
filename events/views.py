from rest_framework import viewsets, permissions, generics
from rest_framework.exceptions import ValidationError
from .models import Event, EventRegistration
from .serializers import EventSerializer, EventRegistrationSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.core.mail import send_mail

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['location', 'date']
    search_fields = ['title', 'description']

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

class EventRegistrationView(generics.CreateAPIView):
    serializer_class = EventRegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        event_id = self.kwargs['event_id']
        event = Event.objects.get(pk=event_id)

        if EventRegistration.objects.filter(event=event, user=self.request.user).exists():
            raise ValidationError("Ти вже зареєстрований на цей івент")

        serializer.save(user=self.request.user, event=event)

        send_mail(
            subject=f'Реєстрація на {event.title}',
            message=f'Привіт, {self.request.user.username}! Ти успішно зареєструвався на {event.title}.',
            from_email='noreply@events.com',
            recipient_list=[self.request.user.email],
            fail_silently=True,
        )