from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('info/<str:name>/<str:payment_id>/', views.info, name="info"),
    path('listing', views.listing, name="listing"),
]
