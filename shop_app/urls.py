from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('checkout/', views.checkout, name="Checkout"),
    path('profile',views.profile,name="profile"),
    path('handlerequest/', views.handlerequest, name="HandleRequest"),
]
