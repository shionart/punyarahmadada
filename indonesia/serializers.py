from indonesia.models import Power
from rest_framework import serializers

class PowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Power
        fields = ['id', 'nama', 'keterangan']