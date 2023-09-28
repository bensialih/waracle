from django.shortcuts import get_object_or_404
from items.models import Cake
from items.serializers import CakeSerializer

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, schema
from rest_framework.schemas import AutoSchema
from rest_framework.views import Response


@api_view(['GET'])
@schema(AutoSchema())
def cakes_all(request):
    return Response(CakeSerializer(Cake.objects.all(), many=True).data)


@api_view(['DELETE'])
@schema(AutoSchema())
def cakes_delete(request, pk: str):
    cake = get_object_or_404(Cake, pk=pk)
    cake.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@schema(AutoSchema())
def cakes_add_one(request):
    serializer = CakeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
