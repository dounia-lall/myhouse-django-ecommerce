
from django.urls import path
from . import views

urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    path('payments/', views.payments,name='payments'),
    path('demo_payment/<str:order_number>/', views.demo_payment, name='demo_payment'),
    path('order_complete/', views.order_complete,name='order_complete'),
]
