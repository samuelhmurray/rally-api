from rest_framework import serializers, viewsets, permissions
from rest_framework.response import Response
from ..models import Community


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = "__all__"


class CommunityViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        needs = Community.objects.all()
        serializer = CommunitySerializer(needs, many=True, context={"request": request})
        return Response(serializer.data)
