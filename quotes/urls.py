from django.urls import path
from .views import QuoteCreateView, QuoteListView

urlpatterns = [
    path('', QuoteCreateView.as_view(), name='quote-create'),  
    path('list/', QuoteListView.as_view(), name='quote-list'),  
]
