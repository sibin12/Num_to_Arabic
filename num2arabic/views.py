from rest_framework import views
from rest_framework.response import Response
from num2words import num2words
from .serializer import NumberSerializer

class NumberToArabicAPIView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = NumberSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        number = serializer.validated_data['number']
        arabic_words = num2words(number, lang='ar')
        return Response({'arabic_words': arabic_words})
