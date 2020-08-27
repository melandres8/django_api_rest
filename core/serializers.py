from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    """ Transformation between our post model
        into a JSON payload, that contains those
        fields on that model.
    """
    class Meta:
        model = Post
        fields = (
            'title',
            'description',
            'owner',
        )
