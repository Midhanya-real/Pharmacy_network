from django.urls import path

from Pharmacy_network.Services import pharmacy_get, medication_get, medication_post

urlpatterns = [
    path('all/', pharmacy_get.pharmacy_all),
    path('all/city=<city>', pharmacy_get.pharmacy_in_city),
    path('detail/<key>', pharmacy_get.pharmacy_element),
    path('detail/<key>/items', medication_get.stuff_in_pharmacy),
    path('add_item/', medication_post.stuff_add_in_pharmacy),

    path('medication/all/', medication_get.stuff_all),
    path('medication/detail/<key>', medication_get.stuff_element),
    path('medication/add/', medication_post.stuff_add),
    path('medication/update/<key>', medication_post.stuff_update),
]