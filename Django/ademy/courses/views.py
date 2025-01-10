#hay que manejar las variables con PascalCase


from django.shortcuts import render, get_object_or_404     #esta linea sirve para renderizar la pagina
from django.http import HttpResponse    #esta linea sirve para enviar un mensaje de respuesta
from .models import Course, Lesson             #esta linea sirve para importar la clase course de la aplicacion models

def course_list(request):               #esta linea sirve para definir una funcion que se llama course_list que recibe un objeto request
    courses = Course.objects.all()      #esta linea sirve para obtener todos los cursos de la base de datos
    contacto = 'danielsamuel1998@contacto.com'
    return render(request,'courses/course_list.html', {'courses': courses, 'contacto':contacto}) #esta linea sirve para renderizar la pagina course_list.html y pasarle los cursos como un objeto de tipo diccion


def course_detail(request, pk):         #esta linea sirve para definir una funcion que se llama course_detail que recibe un objeto request y un objeto pk
    course = get_object_or_404(Course, pk=pk)  #esta linea sirve para obtener el curso con el id que se pasa a la funcion
    return render(request, 'courses/course_detail.html', {'course': course})        #esta linea sirve para renderizar la pagina course_detail.html y pasarle el curso como un objeto de tipo diccionario


def lesson_detail(request, course_pk, lesson_pk):
    lesson = get_object_or_404(Lesson, course_id=course_pk, pk=lesson_pk)
    return render(request, 'courses/lesson_detail.html', {'lesson': lesson})
# Create your views here.
