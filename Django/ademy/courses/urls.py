from django.urls import path, include
from . import views

app_name = 'courses'
urlpatterns = [
    path('', views.course_list, name='course_list'), #de aqui podemos incluso sacar mas endpoints dentro de la cadena vacia bastaria con ponerle nombre
    path('<int:course_pk>/<int:lesson_pk>/', views.lesson_detail, name='lesson_detail'),  #hay que verificar siempre que este bien escrito las llaves primarias
    path('<int:pk>/', views.course_detail, name='detail'), #el nombre que toma es el que se tiene que poner en los HTML para hacer la referencia hacia esas paginas
    
]

#las rutas estan siendo delimitadas del siguiente modo
# se inicia con simbolo de etiquetas <>
#dentro de las etiquetas se hace la referenci al path en donde caera
# en estos casos esta buscando un entero que sea pk / seguido de otro entero que sea lesson_pk
# si no encuentra el entero que se le pide, entonces no se ejecuta la funcion