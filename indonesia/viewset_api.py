from indonesia.models import Power
from indonesia.serializers import PowerSerializer
from rest_framework import viewsets

class PowerViewSet(viewsets.ModelViewSet):
	queryset = Power.objects.all()
	serializer_class = PowerSerializer