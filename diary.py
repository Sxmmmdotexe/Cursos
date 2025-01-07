from collections import OrderedDict
from peewee import *
import datetime
import sys

db = SqliteDatabase('diary.db')

class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default= datetime.datetime.now)
    
    class Meta:     #hay que asegurarnos que las clases esten bien escritas, ya que se determinan con keysensitive
        database = db
        
def add_entry():
    """Agrega un registro"""
    print("Ingresa una entrada. Presiona Ctrl + Z + enter, cuando termines") 
    data = sys.stdin.read().strip()
    if data:
        if input('Guardar entrada? [Y/N]').lower() != 'n':
            Entry.create(content=data)
            print('Almacenamiento exitoso')


def view_entry(search_query=None):
    """Despliega los registros""" 
    entries = Entry.select().order_by(Entry.timestamp.desc())
    
    if search_query:
        entries = entries.where(Entry.content.contains(search_query))
    
    for entry in entries:
        timestamp = entry.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        clear()
        print(f'{timestamp}\n{entry.content}\n')
        print('n | siguiente entrada')
        print('d | eliminar entrada')
        print('q | salir al menu')
        
        next_action = input('Accion a realizar: [Ndq]').lower().strip()
        
        if next_action == 'q':
            break
        elif next_action == 'd':
            confirm = input('¿Estas seguro de eliminar esta entrada? [Y/N]').lower()
            if confirm == 'y':
                delete_entry(entry)

def search_entry():
    """Busca un registro en especifico"""
    view_entry(input('Texto a buscar: \n'))


def delete_entry(entry):
    """Elimina un registro"""
    response = input('¿Completamente seguro? [Y/N]').lower().strip()
    if response == 'y':
        entry.delete_instance()
        print('Eliminado exitosamente \n')

menu = OrderedDict([
    ("a",add_entry),
    ("b",view_entry),
    ("c",delete_entry),
    ("d",search_entry)
])

def menu_loop():
    """Muestra el menu con las opciones"""    
    choice = None
    
    while choice != 'q':
        print("Presiona 'q' para salir")
        for key, value in menu.items():
            print(f'{key} | {value.__doc__}')
        choice = input('Eleccion: ').lower().strip()
    
        if choice in menu:                          #el problema que tenia era que no tenia bien identado el bloque de codigo
            print(f'Ejecutando opcion: {choice}')
            menu[choice]()
        else:
            print(f'Opcion invalida: {choice}')


def initialize():
    db.connect()
    db.create_tables([Entry], safe=True)


if __name__ == '__main__':
    initialize()
    menu_loop()