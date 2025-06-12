from django.shortcuts import render
from rest_framework import viewsets
from .models import IPO
from .serializers import IPOSerializer

# Homepage View
def home(request):
    ipos = IPO.objects.all()
    return render(request, 'home.html', {'ipos': ipos})

# API View
class IPOViewSet(viewsets.ModelViewSet):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer
