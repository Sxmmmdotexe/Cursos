from django.db import models        #esta linea importa el modelo de base de datos de django

class Course(models.Model):         #esta linea define una clase llamada Course que hereda de models.Model
    created_at = models.DateTimeField(auto_now_add=True)   #esta linea define un campo llamado created_at que es de tipo DateTimeField y que se llena automaticamente con el tiempo en el que se creo el registro
    title = models.CharField(max_length=255)    #esta linea define un campo llamado title que es de tipo CharField y que puede contener hasta 255 caracteres
    description = models.TextField()            #esta linea define un campo llamado description que es de tipo TextField y que puede contener texto sin limite de caracteres
    
    #Siempre verificar la identacion de los bloques de codigo
    
    def __str__(self):      #esta linea define un metodo llamado __str__ que devuelve una cadena de texto que representa al objeto
        return self.title       #esta linea retorna el valor del campo title como una cadena de texto
    
    
class Lesson(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    content = models.TextField(blank=True, default='')
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete=models.CASCADE) #esta linea define un campo llamado Course que es de tipo ForeignKey y que hace referencia a la clase Course
    #on_delete = models.cascade es especificada para que cuando se elimine un curso, se eliminen todas las lecciones que pertenecen a ese curso
    class Meta:     #para que sirve el class meta? es para definir metadatos de la clase y esta linea sirve para definir metadatos de la clase Lesson
        ordering = ['order',]        #esta linea define un atributo llamado ordering que especifica la forma en que se ordenan los objetos de la clase Lesson en la base de datos
    
    def __str__(self):
        return self.title
    
    
# Create your models here.
