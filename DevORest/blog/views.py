from django.shortcuts import render
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import blog
from .serializers import BlogSerializer


class blogview(viewsets.ModelViewSet):
    queryset = blog.objects.all()
    serializer_class = BlogSerializer