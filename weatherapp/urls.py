from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index),
   # path('search/', SearchResultsView.as_view(), name='search_results'),
   # path('', HomePageView.as_view(), name='home'),
]