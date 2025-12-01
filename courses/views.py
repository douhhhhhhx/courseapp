from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from django.db.models import Q

from .models import Course, StudentCourse 
from .serializers import  CourseSerializer, StudentCourseSerializer 
 

@api_view(['POST']) 
def add_course(request): 
    serializer = CourseSerializer(data=request.data) 
    if serializer.is_valid(): 
        serializer.save() 
        return Response({"message": "New course is added"}) 
    return Response(serializer.errors, status=400) 
 
@api_view(['GET']) 
def get_all_courses(request): 
    courses = Course.objects.all() 
    serializer = CourseSerializer(courses, many=True) 
    return Response(serializer.data)

@api_view (['PUT'])
def update_course(request,id):
    course=Course.objects.get(pk=id)
    serializer=CourseSerializer(course,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": " course {course.name} is updated"})
    return Response(serializer.errors, status=400) 
 
    
@api_view(['DELETE'])
def delete_course(request,id):
    course=Course.objects.get(pk=id)
    course.delete()
    return Response({"message": "Course deleted successfully"})

@api_view(['GET']) 
def get_courses(request ):
    data=request.GET.get('search','')
    courses=Course.objects.filter(
    Q(name__icontains=data) | 
    Q(instructor__icontains=data) | 
    Q(category__icontains=data)
   )
    serializer=CourseSerializer(courses,many=True)
    return Response(serializer.data)


#association student course

@api_view(['POST']) 
def add_student_course(request): 
    serializer = StudentCourseSerializer(data=request.data) 
    if serializer.is_valid(): 
        serializer.save() 
        return Response({"message": "New studentcourse is added"}) 
    return Response(serializer.errors, status=400) 
 

@api_view(['DELETE'])
def delete_student_course(request,id):
    studnetcourse=StudentCourse.objects.get(pk=id)
    studnetcourse.delete()
    return Response({"message": "studentCourse deleted successfully"})

@api_view (['PUT'])
def update_student_course(request,id):
    studentcourse=Course.objects.get(pk=id)
    serializer=StudentCourseSerializer(studentcourse,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": " studentcourseis updated"})
    return Response(serializer.errors, status=400) 

@api_view(['GET']) 
def get_all_student_courses(request): 
    studentcourses = StudentCourse.objects.all() 
    serializer = StudentCourseSerializer(studentcourses, many=True) 
    return Response(serializer.data)