from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Event;
# Create your views here.

class EventsSerialize(serializers.Serializer):
    event_name = serializers.CharField(read_only=True)
    event_date = serializers.DateField()

@api_view(['GET'])
def events_list(request):
    events = Event.objects.all()
    serialize = EventsSerialize(events, many=True)

    return Response(serialize.data)