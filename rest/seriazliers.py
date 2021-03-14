from rest_framework import serializers

from rest.models import Notes


class NotesSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False)

    class Meta:
        model = Notes
        fields = ['id', 'title', 'content']
