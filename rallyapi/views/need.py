from rest_framework import serializers, viewsets, permissions
from rest_framework.response import Response
from ..models import Community, Need
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

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
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        needs = Need.objects.all()
        serializer = NeedSerializer(needs, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            user_id = int(pk)
        except ValueError:
            return Response({'error': 'Invalid user ID'}, status=status.HTTP_400_BAD_REQUEST)

        needs = Need.objects.filter(user_id=user_id)
        serializer = NeedSerializer(needs, many=True, context={'request': request})
        return Response(serializer.data)
