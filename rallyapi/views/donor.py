from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from ..models import Donor, DonorNeed

class DonorViewSet(viewsets.ViewSet):
    
    @action(detail=False, methods=['post'])
    def claim(self, request):
        user_id = request.data.get('user_id')
        need_id = request.data.get('need_id')
        donor_type_id = request.data.get('donor_type_id')
        donor, _ = Donor.objects.get_or_create(user_id=user_id, type_id=donor_type_id)
        DonorNeed.objects.create(donor_id=donor.id, need_id=need_id)

        return Response({'message': 'Claimed successfully'}, status=status.HTTP_200_OK)
