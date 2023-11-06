from django.shortcuts import render
from rest_framework import generics, serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Heroes
from .serializers import HeroesSerializer


class HeroesAPIViewList(generics.ListCreateAPIView):
    queryset = Heroes.objects.all()
    serializer_class = HeroesSerializer


class HeroesAPIViewUpdate(generics.UpdateAPIView):
    queryset = Heroes.objects.all()
    serializer_class = HeroesSerializer


class HeroesAPIViewCRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Heroes.objects.all()
    serializer_class = HeroesSerializer

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
