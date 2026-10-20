from datos.repositorios.repo_articulo import RepoArticulo

def publicar_nueva_noticia(titulo, contenido, autor_id, categoria_id):
        
        if not titulo or len(titulo) < 5:
            raise ValueError("El titular de la noticia debe tener al menos 5 caracteres.")
        if not contenido:
            raise ValueError("El cuerpo de la noticia no puede estar vacío.")
        
        return RepoArticulo.guardar_articulo(titulo, contenido, autor_id, categoria_id)

def listar_noticias_canal():
        return RepoArticulo.obtener_todos()
