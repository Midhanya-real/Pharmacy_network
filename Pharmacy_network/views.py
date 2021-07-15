from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from pharmacy_network.models import Pharmacy, Stuff, Pharmacy_staff
from pharmacy_network.serializers import Pharmacy_all_serializer, Pharmacy_detail_serializer, Stuff_all_serializer, \
    Stuff_detail_serializer, StuffIn_pharmacy_add_serializer, Stuff_in_pharmacy_serializer


class Pharmacy_list(APIView):

    def get(self, request):
        pharmacy = Pharmacy.objects.all()
        serializer = Pharmacy_all_serializer(pharmacy, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Pharmacy_detail(APIView):

    def get_object(self, pk):
        try:
            return Pharmacy.objects.get(pk=pk)
        except Pharmacy.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pharmacy = self.get_object(pk)
        serializer = Pharmacy_detail_serializer(pharmacy)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Pharmacy_city_filter(APIView):
    def get_object(self, city):
        try:
            return Pharmacy.objects.filter(address__contains=city)
        except Pharmacy.DoesNotExist:
            raise Http404

    def get(self, request, city):
        pharmacy = self.get_object(city)
        serializer = Pharmacy_all_serializer(pharmacy, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Medication_list(APIView):
    def get(self, request):
        stuff = Stuff.objects.all()
        serializer = Stuff_all_serializer(stuff, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Medication_detail(APIView):
    def get_object(self, pk):
        try:
            return Stuff.objects.get(pk=pk)
        except Stuff.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        stuff = self.get_object(pk)
        serializer = Stuff_detail_serializer(stuff)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = Stuff_detail_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        stuff = self.get_object(pk)
        serializer = Stuff_detail_serializer(stuff, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Add_medication_in_pharmacy(APIView):
    def get_object(self, pk):
        try:
            return Stuff.objects.get(pk=pk)
        except Stuff.DoesNotExist:
            raise Http404

    def post(self, request):
        stuff = self.get_object(request.data['stuff'])
        serializer = StuffIn_pharmacy_add_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class Pharmacy_stuff_list(APIView):
    def get_object(self, pk):
        try:
            return Pharmacy_staff.objects.filter(pharmacy=pk)
        except Pharmacy.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        stuff_in_pharmacy = self.get_object(pk)
        serializer = Stuff_in_pharmacy_serializer(stuff_in_pharmacy, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
