from Capitulo import claseCapitulo
import re
class claseLibro:
    __idLibro = 0   #ID del libro
    __titulo = ''   #título del libro
    __autor = ''    #autor del libro
    __editorial = ''    #editorial del libro
    __isbn = 0  #numero internacional
    __cantidadCapitulos = 0 #cantidad de capítulos del libro
    __capitulos = []   #capítulo
    def __init__(self, id = '0', titulo = '', autor = '', editorial = '', isbn = '0', cantCap = '0'):
        self.__idLibro = id
        self.__titulo = titulo
        self.__autor = autor
        self.__editorial = editorial
        self.__isbn = int(isbn)
        self.__cantidadCapitulos = int(cantCap)
    def crearListaCap(self, reader):
        i = self.__cantidadCapitulos
        lista = []
        for fila in reader:
            unCap = claseCapitulo(fila[0], fila[1])
            lista.append(unCap)
            i-=1
            if(i == 0):
                break
        self.__capitulos = lista.copy()
    def getId(self):
        return self.__idLibro
    def getTitulo(self):
        return self.__titulo
    def getAutor(self):
        return self.__autor
    def getCaps(self):
        return self.__capitulos
    def mostrar(self):
        cabeza = """\
        +-----------------------------------------------------------------------------------------------------+
        | {:5} {:40} {:20} {:16} {:10} {:1} |
        +-----------------------------------------------------------------------------------------------------+\
        """
        cuerpo = """\
        | {} |\
        """
        print(cabeza.format(self.__idLibro, self.__titulo, self.__autor, self.__editorial, self.__isbn,
                             self.__cantidadCapitulos))
        for i in range(len(self.__capitulos)):
            print(cuerpo.format(self.__capitulos[i]))
