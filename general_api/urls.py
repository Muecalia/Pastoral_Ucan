from django.contrib import admin
from django.urls import path
from .views import AcademicLevelView, TypeActivityView

urlpatterns = [
    path('academic_level', AcademicLevelView.as_view(), name='academic_level'),
    path('type_activity', TypeActivityView.as_view(), name='type_activity'),
]
