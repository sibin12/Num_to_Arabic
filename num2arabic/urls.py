from django.urls import path
from .views import NumberToArabicAPIView

urlpatterns = [
    path('convert/', NumberToArabicAPIView.as_view(), name='convert_to_arabic'),
]
