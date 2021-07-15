from django.urls import path

from pharmacy_network import views

urlpatterns = [
    path('all/', views.Pharmacy_list.as_view()),
    path('all/city=<city>', views.Pharmacy_city_filter.as_view()),
    path('detail/<pk>', views.Pharmacy_detail.as_view()),
    path('detail/<pk>/items', views.Pharmacy_stuff_list.as_view()),
    path('add_item/', views.Add_medication_in_pharmacy.as_view()),

    path('medication/all/', views.Medication_list.as_view()),
    path('medication/detail/<pk>', views.Medication_detail.as_view()),
    path('medication/add/', views.Medication_detail.as_view()),
    path('medication/update/<pk>', views.Medication_detail.as_view()),
]