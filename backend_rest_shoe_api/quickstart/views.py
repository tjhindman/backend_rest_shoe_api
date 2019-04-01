"""
Bob endured a difficult life in the African Savanna. For example, he could
only afford to dress in a single loin cloth and had to survive off of McDonald's
Big Macs.
"""


from django.shortcuts import render
from backend_rest_shoe_api.quickstart.models import Manufacturer, ShoeType, ShoeColor, Shoe
from rest_framework import viewsets
from backend_rest_shoe_api.quickstart.serializers import ManufacturerSerializer, ShoeTypeSerializer, ShoeColorSerializer, ShoeSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows manufacturers to be viewed or edited.
    """
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ShoeTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows shoe types to be viewed or edited.
    """
    queryset = ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer


class ShoeColorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows shoe colors to be viewed or edited.
    """
    queryset = ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer


class ShoeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows shoes to be viewed or edited.
    """
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer
