from datos.conexion_db import db, conectar, cerrar
from datos.modelos.models import Rol, Usuario, Autor, Categoria, EstadoArticulo, Articulo, Lector, Plan, Suscripcion, Comentario, Like
from auxiliares.opciones_menu import obtener_menu_principal
from presentacion.menu import InterfazConsola
from negocio.negocio_articulos import NegocioArticulos
import os

def inicializar_datos_prueba():
    db.create_tables([Rol, Usuario, Autor, Categoria, EstadoArticulo, Articulo, Lector, Plan, Suscripcion, Comentario, Like])
    
    if Categoria.select().count() == 0:
        cat_politica = Categoria.create(nombre="Política Nacional")
        cat_deportes = Categoria.create(nombre="Deportes")
        
        rol_admin = Rol.create(nombre="Editor General", permisos="ALL")
        usr = Usuario.create(nombre="Carlos Redactor", correo="carlos@noticias.com", contrasena="123", rol=rol_admin)
        periodista = Autor.create(nombre="Carlos Mendoza", biografia="Reportero de investigación con 10 años de experiencia.", usuario=usr)
        
        NegocioArticulos.publicar_nueva_noticia(
            "Histórica votación en el congreso aprueba reformas clave", 
            "En una jornada intensa, los parlamentarios dieron luz verde al proyecto de ley...", 
            periodista.id, 
            cat_politica.id
        )
        NegocioArticulos.publicar_nueva_noticia(
            "La Roja clasifica al mundial despues de más de una decada de espera.", 
            "Cogoteo en puente alto...", 
            periodista.id, 
            cat_deportes.id
        )
        
        Lector.create(nombre="Ana Gómez", correo="ana.gomez@gmail.com")
        Lector.create(nombre="Juan Pérez", correo="juan.perez@hotmail.com")

def main():
    conectar()
    inicializar_datos_prueba()
    
    while True:
        print(obtener_menu_principal())
        opcion = input().strip()
        
        if opcion == "1":
            InterfazConsola.mostrar_articulos()
        elif opcion == "2":
            InterfazConsola.mostrar_autores()
        elif opcion == "3":
            InterfazConsola.mostrar_audiencia()
        elif opcion == "4":
            print("Hata la proxima")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
            
    cerrar()

if __name__ == "__main__":
    main()
