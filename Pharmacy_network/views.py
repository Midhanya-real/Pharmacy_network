from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from pharmacy_network.models import Pharmacy, Stuff, Pharmacy_staff
from pharmacy_network.serializers import PharmacyAllSerializer, PharmacyDetailSerializer, StuffAllSerializer, \
    StuffDetailSerializer, StuffInPharmacyAdd, StuffInPharmacy


class PharmacyList(APIView):

    def get(self, request, format=None):
        pharmacy = Pharmacy.objects.all()
        serializer = PharmacyAllSerializer(pharmacy, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PharmacyDetail(APIView):

    def get_object(self, pk):
        try:
            pharmacy = Pharmacy.objects.get(pk=pk)
        except Pharmacy.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pharamcy = self.get_object(pk)
        serializer = PharmacyDetailSerializer(pharamcy)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PharmacyCityFilter(APIView):
    def get_object(self, city):
        try:
            pharmacy = Pharmacy.objects.filter(address__contains=city)
        except Pharmacy.DoesNotExist:
            raise Http404

    def get(self, request, city, format=None):
        pharamcy = self.get_object(city)
        serializer = PharmacyAllSerializer(pharamcy)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MedicationList(APIView):
    def get(self, request, format=None):
        stuff = Stuff.objects.all()
        serializer = StuffAllSerializer(stuff, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MedicationDetail(APIView):
    def get_object(self, pk):
        try:
            stuff = Stuff.objects.get(pk=pk)
        except Stuff.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        stuff = self.get_object(pk)
        serializer = StuffDetailSerializer(stuff)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StuffDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        stuff = self.get_object(pk)
        serializer = StuffDetailSerializer(stuff, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddMedicationInPharmacy(APIView):
    def get_object(self, pk):
        try:
            stuff = Stuff.objects.get(pk=pk)
        except Stuff.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        stuff = self.get_object(request.data['stuff'])
        serializer = StuffInPharmacyAdd(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class PharmacyStuffList(APIView):
    def get_object(self, pk):
        try:
            pharmacy = Pharmacy_staff.objects.filter(pharmacy=pk)
        except Pharmacy.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        stuff = self.get_object(pk),
        serializer = StuffInPharmacy(stuff, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
