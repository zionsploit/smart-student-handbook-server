from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import events_list

urlpatterns = [
    path('get-all-events', events_list)
]

urlpatterns = format_suffix_patterns(urlpatterns)