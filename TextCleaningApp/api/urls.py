from django.urls import path
from .views import CleanTextView

urlpatterns = [
    path('clean/', CleanTextView.as_view(), name='clean_text'),
]
