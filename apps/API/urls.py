from . import views
from django.urls import path

urlpatterns = [
    path('assistenceList/', views.getAssistenceList, name="assistenceList"),
]
