from rest_framework import status
from rest_framework import serializers, viewsets, permissions
from rest_framework.response import Response
from ..models import Community, Need, Donor, Type, DonorNeed
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email']

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class DonorSerializer(serializers.ModelSerializer):
    type = TypeSerializer(many=False)
    user = UserSerializer(many=False)
    id = serializers.IntegerField(source='pk')  # Add this line

    class Meta:
        model = Donor
        fields = ['id', 'user', 'type']
        
class DonorNeedSerializer(serializers.ModelSerializer):
    donor_type = TypeSerializer(many=False, source='donor.type')  # Adjust source

    class Meta:
        model = DonorNeed
        fields = ['id', 'need', 'donor', 'donor_type']


class NeedSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    community = CommunitySerializer()
    donors = DonorSerializer(many=True)
    donor_needs = DonorNeedSerializer(source='donorneed_set', many=True, read_only=True)

    class Meta:
        model = Need
        fields = ['id', 'title', 'description', 'date_posted', 'complete', 'user', 'community', 'donors', 'donor_needs']

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
    
    def destroy(self, request, pk=None):
        try:
            need = Need.objects.get(pk=pk)
        except Need.DoesNotExist:
            return Response({'error': 'Need not found'}, status=status.HTTP_404_NOT_FOUND)

        need.delete()
        return Response({'message': 'Need deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
