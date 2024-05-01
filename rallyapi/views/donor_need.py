from rest_framework import viewsets, status, serializers
from rest_framework.response import Response
from ..models import DonorNeed
from rest_framework.decorators import action

class DonorNeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonorNeed
        fields = '__all__'
        
class DonorNeedViewSet(viewsets.ViewSet):
    
    def retrieve(self, request, pk=None):
        try:
            donor_need = DonorNeed.objects.get(pk=pk)
        except DonorNeed.DoesNotExist:
            return Response({'error': 'DonorNeed not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DonorNeedSerializer(donor_need)
        return Response(serializer.data)
    

    def destroy(self, request, pk=None):
        try:
            donor_need = DonorNeed.objects.get(pk=pk)
        except DonorNeed.DoesNotExist:
            return Response({'error': 'DonorNeed not found'}, status=status.HTTP_404_NOT_FOUND)

        donor_need.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)