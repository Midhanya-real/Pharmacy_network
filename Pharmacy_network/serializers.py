from rest_framework import serializers
from Pharmacy_network.models import Pharmacy, Stuff, Pharmacy_staff


class PharmacyAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = ('name', 'address')


class PharmacyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = ('name', 'address', 'open_date', 'close_date',)


class StuffAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stuff
        fields = ('name', 'price')


class StuffDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stuff
        fields = ('name', 'price', 'volume', 'country', 'date',)


class StuffInPharmacyAdd(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy_staff
        fields = ('pharmacy', 'stuff',)


class StuffInPharmacy(serializers.ModelSerializer):
    pharmacy = PharmacyAllSerializer(read_only=True)
    stuff = StuffDetailSerializer(read_only=True)

    class Meta:
        model = Pharmacy_staff
        fields = ('pharmacy', 'stuff',)
