import re
class claseCapitulo:
    __titulo = ''   #título del capítulo
    __cantidadPaginas = 0   #cantidad de páginas del capítulo
    def __init__(self, titulo = '', pags = '0'):
        self.__titulo = titulo
        self.__cantidadPaginas = pags
    def __str__(self):
        return "{:20}: {:3}".format(self.__titulo, self.__cantidadPaginas)
    def getTitulo(self):
        return self.__titulo
    def getPags(self):
        return self.__cantidadPaginas