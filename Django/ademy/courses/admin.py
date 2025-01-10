from django.contrib import admin    #esta linea es para importar el modulo admin

from .models import Course, Lesson  #esta linea importa las clases de los modelos de la app desde models.py

class LessonInline(admin.StackedInline):  #el stacked inline es para que se vea la informacion de la relacion en forma de bloques y el tabular en forma de lista
    model = Lesson

class CourseAdmin(admin.ModelAdmin):    #esta linea es para que se vea la informacion de la relacion en forma de bloques
    inlines = [LessonInline, ]

admin.site.register(Course, CourseAdmin) #esta linea permite agregar el modelo a la interfaz de administracion de django
# Register your models here.
