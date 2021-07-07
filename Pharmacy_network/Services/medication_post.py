from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Pharmacy_network.models import Stuff, Pharmacy
from Pharmacy_network.serializers import StuffDetailSerializer, StuffInPharmacyAdd


@api_view(['POST'])
def stuff_add(request):
    if request.method == 'POST':
        serializer = StuffDetailSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def stuff_update(request, key):
    try:
        stuff = Stuff.objects.get(pk=key)
    except Stuff.DoesNotExist:
        return Response('DATA_NOT_FOUND', status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = StuffDetailSerializer(stuff, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def stuff_add_in_pharmacy(request):
    try:
        stuff = Stuff.objects.get(pk=request.data['stuff'])
    except Stuff.DoesNotExist:
        return Response('DATA_NOT_FOUND', status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serializer = StuffInPharmacyAdd(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
