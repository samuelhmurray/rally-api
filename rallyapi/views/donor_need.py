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
    
    @action(detail=False, methods=['delete'])  
    def unclaim(self, request):
        donor_need_id = request.data.get('donor_need_id') 
        if donor_need_id is None:
            return Response({'error': 'DonorNeed ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            donor_need = DonorNeed.objects.get(pk=donor_need_id)
        except DonorNeed.DoesNotExist:
            return Response({'error': 'DonorNeed not found'}, status=status.HTTP_404_NOT_FOUND)
        
        donor_need.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
