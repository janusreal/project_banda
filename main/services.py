from main.models import *


def crear_artista(nombre,apellido,cantante,instrumento):
    a = Artista(nombre=nombre, apellido=apellido, cantante=cantante, instrumento=instrumento)
    a.save()
    return a

'''relacion_artista_grupo
agregar_album
obtiene_artista
obtiene_grupo
artista_pertenece_a_grupos
artista_participa_albumes
grupo_albumes
'''
