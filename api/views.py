from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from OktaAuth import OktaAuthentication

authentication_classes = [OktaAuthentication]
permission_classes = [IsAuthenticated]


@api_view(['GET'])
def getData(request):
    
    response = {'message': 'This is a open API endpoint.'}
    return Response(response)


