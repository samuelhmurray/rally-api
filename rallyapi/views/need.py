from rest_framework import serializers, viewsets
from rest_framework.response import Response
from ..models import Community, Need
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']  # Include more fields as needed


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'


class NeedSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    community = CommunitySerializer()

    class Meta:
        model = Need
        fields = ['id', 'description', 'date_posted', 'complete', 'user', 'community']


class NeedViewSet(viewsets.ViewSet):
    def list(self, request):
        needs = Need.objects.all()
        serializer = NeedSerializer(needs, many=True, context={'request': request})
        return Response(serializer.data)