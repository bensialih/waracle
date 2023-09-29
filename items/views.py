from items.models import Cake
from items.serializers import CakeSerializer
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import DestroyModelMixin, ListModelMixin
from rest_framework.views import Response


class CakesApi(GenericAPIView, ListModelMixin, DestroyModelMixin):
    serializer_class = CakeSerializer
    queryset = Cake.objects.all()

    def post(self, request):
        '''create a new cakes.'''
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        '''Return a list of all cakes.'''
        return self.list(request)


class CakesDeleteApi(GenericAPIView, DestroyModelMixin):
    serializer_class = CakeSerializer
    queryset = Cake.objects.all()

    def delete(self, request, format=None, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
