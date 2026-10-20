# from peewee import SqliteDatabase
# db = SqliteDatabase('canal_noticias.db')

# def conectar():
#     if db.is_closed():
#         db.connect()

# def cerrar():
#     if not db.is_closed():
#         db.close()

from peewee import *

database = MySQLDatabase('iec_n2_c1', **{'charset': 'utf8mb4', 'host': 'localhost', 'user': 'iec_n2_c1', 'password': 'iecn2c1'})