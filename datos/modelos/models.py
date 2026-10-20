from peewee import Model, CharField, TextField, DateField, DecimalField, IntegerField, ForeignKeyField, BooleanField
from datos.conexion_db import db
import datetime

class BaseModel(Model):
    class Meta:
        database = db

class Rol(BaseModel):
    nombre = CharField(unique=True)
    permisos = TextField()

class Usuario(BaseModel):
    nombre = CharField()
    correo = CharField(unique=True)
    contrasena = CharField()
    rol = ForeignKeyField(Rol, backref='usuarios')

class Autor(BaseModel):
    nombre = CharField()
    biografia = TextField()
    usuario = ForeignKeyField(Usuario, backref='perfil_autor')

class Categoria(BaseModel):
    nombre = CharField(unique=True)

class EstadoArticulo(BaseModel):
    estado = CharField(unique=True)

class Articulo(BaseModel):
    titulo = CharField()
    contenido = TextField()
    fecha_publicacion = DateField(default=datetime.date.today)
    autor = ForeignKeyField(Autor, backref='articulos')
    categoria = ForeignKeyField(Categoria, backref='articulos')
    estado = ForeignKeyField(EstadoArticulo, backref='articulos', null=True)

class Etiqueta(BaseModel):
    nombre = CharField(unique=True)

class Plan(BaseModel):
    nombre = CharField()
    precio = DecimalField(max_digits=10, decimal_places=2)
    duracion = IntegerField()

class Lector(BaseModel):
    nombre = CharField()
    correo = CharField(unique=True)

class Suscripcion(BaseModel):
    lector = ForeignKeyField(Lector, backref='suscripciones')
    plan = ForeignKeyField(Plan, backref='suscripciones')
    fecha_inicio = DateField(default=datetime.date.today)
    fecha_fin = DateField()
    estado = CharField() 

class Comentario(BaseModel):
    contenido = TextField()
    fecha = DateField(default=datetime.date.today)
    lector = ForeignKeyField(Lector, backref='comentarios')
    articulo = ForeignKeyField(Articulo, backref='comentarios')

class Like(BaseModel):
    lector = ForeignKeyField(Lector, backref='likes')
    articulo = ForeignKeyField(Articulo, backref='likes')
    fecha = DateField(default=datetime.date.today)
