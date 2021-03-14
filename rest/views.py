from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from rest.models import Notes
from rest.seriazliers import NotesSerializer


class NotesViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer

    filter_backends = [SearchFilter]
    search_fields = ['title', 'content']
