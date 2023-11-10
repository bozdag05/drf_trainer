from django.shortcuts import render
from rest_framework import generics, serializers, viewsets
from rest_framework.permissions import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsAdminOrReadOnly, IsAuthorAdminOrReadOnly
from .models import Heroes, Category, Gender
from .serializers import HeroesSerializer


# class HeroesViewSet(viewsets.ModelViewSet):
#     queryset = Heroes.objects.all()
#     serializer_class = HeroesSerializer
#
#     @action(methods=["get"], detail=True)
#     def categories(self, request, pk=None):
#         categories = Category.objects.get(pk=pk)
#         return Response({"categories": categories.title})

class HeroesAPIViewList(generics.ListCreateAPIView):
    queryset = Heroes.objects.all()
    serializer_class = HeroesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class HeroesAPIViewUpdate(generics.RetrieveUpdateAPIView):
    queryset = Heroes.objects.all()
    serializer_class = HeroesSerializer
    permission_classes = (IsAuthorAdminOrReadOnly, )


class HeroesAPIViewDestroy(generics.RetrieveDestroyAPIView):
    queryset = Heroes.objects.all()
    serializer_class = HeroesSerializer
    permission_classes = (IsAdminOrReadOnly, )

# class HeroesAPIView(APIView):
#     def get(self, request):
#         array = Heroes.objects.all()
#         return Response({"posts": HeroesSerializer(array, many=True).data})
#
#     def post(self, request):
#         serializer = HeroesSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({"post": serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Нету ключа pk (id)"})
#
#         try:
#             pass
#         except:
#             return Response({"error": "Нету такого объекты, вы шо?"})
#
#         serializer = HeroesSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Нету ключа pk (id)"})
#
#         try:
#             pass
#         except:
#             return Response({"error": "Нету такого объекты, вы шо?"})
#
#         serializer = HeroesSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})

# class HeroesAPIView(generics.ListAPIView):
#     queryset = Heroes.objects.all()
#     serializer_class = HeroesSerializer
