from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.list_resources.as_view(),name='resources-list'),
    path('add/',views.add_hospital.as_view(),name='hospital-add'),
    path('add/resources/',views.add_resource.as_view(),name='resources-add'),
    path('hospital/details/<int:pk>',views.show_hospital_details.as_view(),name='hospital-details'),
    path('update/<int:pk>',views.update_resource.as_view(),name='update-resource'),
    path('delete/<int:pk>',views.delete_resource.as_view(),name='delete-resource'),

    path('hospital/update/<int:pk>',views.update_hospital.as_view(),name='update-hospital'),
    path('hospital/delete/<int:pk>',views.delete_hospital.as_view(),name='delete-hospital'),

    path('booking/book/<int:pk>',views.book_resource,name='book-resource'),
    path('booking/confirmed/<int:pk>',views.book_resource,name='booking-confirmed'),
    # path('booking/delete/<int:id>',views.delete_booking,name='delete-booking'),
]
