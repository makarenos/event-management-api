from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import EventViewSet, EventRegistrationView

router = DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns = router.urls + [
    path('events/<int:event_id>/register/', EventRegistrationView.as_view(), name='event-register'),
]