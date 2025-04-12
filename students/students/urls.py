from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student-list'),
    path('/<int:pk>/', views.student_detail, name='student-detail'),
    path('/studentsub/', views.student_sub_details,name='student-sub-details')
]
