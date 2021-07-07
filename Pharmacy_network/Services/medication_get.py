from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Pharmacy_network.models import Stuff, Pharmacy, Pharmacy_staff
from Pharmacy_network.serializers import StuffAllSerializer, StuffDetailSerializer, StuffInPharmacy


@api_view(['GET'])
def stuff_all(request):
    if request.method == 'GET':
        stuff = Stuff.objects.all()
        serializer = StuffAllSerializer(stuff, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def stuff_element(request, key):
    try:
        stuff = Stuff.objects.get(pk=key)
    except Stuff.DoesNotExist:
        return Response([], status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StuffDetailSerializer(stuff)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def stuff_in_pharmacy(request, key):
    try:
        Pharmacy.objects.get(pk=key)
    except Pharmacy.DoesNotExist:
        return Response([], status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        shuff_in_pharmacy = Pharmacy_staff.objects.filter(pharmacy=key)
        serializer = StuffInPharmacy(shuff_in_pharmacy, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)