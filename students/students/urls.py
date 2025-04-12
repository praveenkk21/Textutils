from django.urls import path
from . import views
from .views import student_sub_details

urlpatterns = [
    path('', views.student_list, name='student-list'),
    path('/<int:pk>/', views.student_detail, name='student-detail'),
    path('studentsub/', student_sub_details.as_view(),name='student-sub-details')
]
