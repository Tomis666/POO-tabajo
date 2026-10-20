from datos.modelos.models import Articulo, Autor, Categoria


def guardar_articulo(titulo, contenido, autor_id, categoria_id):
        return Articulo.save(
            titulo=titulo,
            contenido=contenido,
            autor=autor_id,
            categoria=categoria_id
        )

def obtener_todos():
        return Articulo.select()
