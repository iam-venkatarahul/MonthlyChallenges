from django.urls import path
from . import views

urlpatterns = [
    path("<int:month>" , views.monthly_challenge_number),
    path("<str:month>" , views.monthly_challenge , name="month-chall"),
    path("" , views.index_of_months)
    
]