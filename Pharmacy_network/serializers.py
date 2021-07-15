from rest_framework import serializers
from pharmacy_network.models import Pharmacy, Stuff, Pharmacy_staff


class Pharmacy_all_serializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = ('name', 'address')


class Pharmacy_detail_serializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = ('name', 'address', 'open_date', 'close_date',)


class Stuff_all_serializer(serializers.ModelSerializer):
    class Meta:
        model = Stuff
        fields = ('name', 'price')


class Stuff_detail_serializer(serializers.ModelSerializer):
    class Meta:
        model = Stuff
        fields = ('name', 'price', 'volume', 'country', 'date',)


class StuffIn_pharmacy_add_serializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy_staff
        fields = ('pharmacy', 'stuff',)


class Stuff_in_pharmacy_serializer(serializers.ModelSerializer):
    pharmacy = Pharmacy_all_serializer(read_only=True)
    stuff = Stuff_detail_serializer(read_only=True)

    class Meta:
        model = Pharmacy_staff
        fields = ('pharmacy', 'stuff',)

