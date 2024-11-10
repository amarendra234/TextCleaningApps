import re
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TextSerializer

class CleanTextView(APIView):
    def post(self, request):
        serializer = TextSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            cleaned_text = self.clean_text(text)
            return Response({"cleaned_text": cleaned_text})
        return Response(serializer.errors, status=400)

    def clean_text(self, text):
        text = re.sub(r'\W+', ' ', text)  # Remove special characters
        text = re.sub(r'\s+', ' ', text).strip()  # Remove extra whitespace
        return text
