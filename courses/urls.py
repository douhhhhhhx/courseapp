from django.urls import path 
from . import views 
 
urlpatterns = [
    path('course/add/',views.add_course,name='add_course'),
    path('course/<int:id>/delete/',views.delete_course,name='delete_course'),
    path('course/<int:id>/update/',views.update_course,name='update_course'),
    path('course/getAll/',views.get_all_courses,name='get_all_courses'),
    path('courses/search/', views.get_courses,name="course_search"),
    # Student-Course
    path('studentcourse/', views.get_all_student_courses,name="get_all_student_courses"),     
    path('studentcourse/add/', views.add_student_course,name="studentcourse_add"),         
    path('studentcourse/<int:id>/delete/', views.delete_student_course,name="studentcourse_delete"), 
    path('studentcourse/<int:id>/update/', views.update_student_course,name="studentcourse_update"),  
]
