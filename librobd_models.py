
from peewee import *

database = MySQLDatabase('librobd', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': 'localhost', 'user': 'root'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Autores(BaseModel):
    nombre = CharField(unique=True)

    class Meta:
        table_name = 'autores'

class Libros(BaseModel):
    autor = ForeignKeyField(column_name='autor_id', field='id', model=Autores)
    cantidad = IntegerField()
    precio = DecimalField()
    titulo = CharField()

    class Meta:
        table_name = 'libros'

