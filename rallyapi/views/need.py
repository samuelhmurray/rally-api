from rest_framework import status
from rest_framework import serializers, viewsets, permissions
from rest_framework.response import Response
from ..models import Community, Need, Donor, Type, DonorNeed
from django.contrib.auth.models import User
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404


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

class BasicNeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Need
        fields = ['id', 'title', 'description', 'date_posted', 'complete', 'community', 'user']

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
    
    def create(self, request):
        serializer = BasicNeedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None): 
        try:
            need = Need.objects.get(pk=pk)
        except Need.DoesNotExist:
            return Response({'error': 'Need not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BasicNeedSerializer(need, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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
    
    @action(detail=True, methods=['get'])
    def get_need_by_user_and_need_id(self, request, user_id=None, pk=None):
        try:
            user_id = int(user_id)
            pk = int(pk)
        except ValueError:
            return Response({'error': 'Invalid user ID or need ID'}, status=status.HTTP_400_BAD_REQUEST)

        need = get_object_or_404(Need, pk=pk, user_id=user_id)
        serializer = NeedSerializer(need)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def get_need_by_need_id(self, request, pk=None):
        try:
            pk = int(pk)
        except ValueError:
            return Response({'error': 'Invalid user ID or need ID'}, status=status.HTTP_400_BAD_REQUEST)

        need = get_object_or_404(Need, pk=pk)
        serializer = NeedSerializer(need)
        return Response(serializer.data)