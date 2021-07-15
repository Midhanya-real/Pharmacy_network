from django.urls import path

from pharmacy_network import views

urlpatterns = [
    path('all/', views.PharmacyList.as_view()),
    path('all/city=<city>', views.PharmacyCityFilter.as_view()),
    path('detail/<pk>', views.PharmacyDetail.as_view()),
    path('detail/<pk>/items', views.PharmacyStuffList.as_view()),
    path('add_item/', views.AddMedicationInPharmacy.as_view()),

    path('medication/all/', views.MedicationList.as_view()),
    path('medication/detail/<pk>', views.MedicationDetail.as_view()),
    path('medication/add/', views.MedicationDetail.as_view()),
    path('medication/update/<pk>', views.MedicationDetail.as_view()),
]