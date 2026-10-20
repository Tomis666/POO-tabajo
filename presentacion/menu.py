from prettytable import PrettyTable
from negocio.negocio_articulos import NegocioArticulos
from datos.modelos.models import Autor, Lector, Plan

class InterfazConsola:
    @staticmethod
    def mostrar_articulos():
        articulos = NegocioArticulos.listar_noticias_canal()
        
        
        tabla = PrettyTable()
        tabla.field_names = ["ID", "Titular de la Noticia", "Sección / Categoría", "Periodista (Autor)", "Fecha"]
        tabla.align["Titular de la Noticia"] = "l" 
        
        for art in articulos:
            tabla.add_row([art.id, art.titulo, art.categoria.nombre, art.autor.nombre, art.fecha_publicacion])
            
        print("\n=== CRÓNICAS Y ARTÍCULOS PUBLICADOS ===")
        print(tabla)

    @staticmethod
    def mostrar_autores():
        autores = Autor.select()
        tabla = PrettyTable()
        tabla.field_names = ["ID", "Nombre del Periodista", "Perfil / Biografía"]
        tabla.align["Perfil, Biografía"] = "l"
        
        for aut in autores:
            tabla.add_row([aut.id, aut.nombre, aut.biografia[:60] + "..."])
            
        print("\n=== PLANTILLA DE PERIODISTAS Y AUTORES ===")
        print(tabla)

    @staticmethod
    def mostrar_audiencia():
        lectores = Lector.select()
        tabla = PrettyTable()
        tabla.field_names = ["ID Lector", "Nombre Completo", "Correo Electrónico"]
        
        for lec in lectores:
            tabla.add_row([lec.id, lec.nombre, lec.correo])
            
        print("\n=== REGISTRO DE AUDIENCIA DIGITAL ===")
        print(tabla)
