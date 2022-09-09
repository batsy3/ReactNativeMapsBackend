from rest_framework import serializers
from models.coordinates import Area

class CoordinateSerializer(serializers.ModelSerializer):
    class Mwta:
        model = Area
        fields = "__all__"