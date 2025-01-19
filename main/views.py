from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Endpoint
from .serializers import EndpointSerializer

class EndpointList(APIView):
    def get(self, request):
        """Получить список всех доступных эндпоинтов"""
        endpoints = Endpoint.objects.all()
        serializer = EndpointSerializer(endpoints, many=True)
        return Response(serializer.data)
