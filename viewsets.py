from .models import Aluno
from .serializer import AlunoSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import DjangoObjectPermissions
from rest_framework.generics import GenericAPIView

class AlunoViewSet(viewsets.ViewSet, GenericAPIView):

    serializer_class = AlunoSerializer
    queryset = Aluno.objects.all()
    permission_classes = [DjangoObjectPermissions]

    def list (self, request):
        
        serializer = AlunoSerializer(Aluno.objects.all(), many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk):
        item = Aluno.objects.get(pk=pk)
        serializer = AlunoSerializer(item, data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = AlunoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
    def partial_update(self, request, *args, **kwargs):
        
        item = Aluno.objects.get(pk=kwargs.get('pk'))
        serializer = AlunoSerializer(item, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def destroy(self, request, pk):
        item = Aluno.objects.get(pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#class AlunoViewSet(viewsets.ModelViewSet):
#
#   queryset = Aluno.objects.all()
#  serializer_class = AlunoSerializer
