from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Pharmacy_network.models import Pharmacy
from Pharmacy_network.serializers import PharmacyAllSerializer, PharmacyDetailSerializer


@api_view(['GET'])
def pharmacy_all(request):

    if request.method == 'GET':
        pharmacy = Pharmacy.objects.all()
        serializer = PharmacyAllSerializer(pharmacy, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def pharmacy_element(request, key):

    try:
        pharmacy = Pharmacy.objects.get(pk=key)
    except Pharmacy.DoesNotExist:
        return Response([], status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PharmacyDetailSerializer(pharmacy)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def pharmacy_in_city(request, city):

    try:
        pharmacy = Pharmacy.objects.filter(address__contains=city)
    except Pharmacy.DoesNotExist:
        return Response('DATA_NOT_FOUND', status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PharmacyAllSerializer(pharmacy, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)