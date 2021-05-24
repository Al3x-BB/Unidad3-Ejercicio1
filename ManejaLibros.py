from Libro import claseLibro
import re
import csv
class claseManejaLibros:
    __lista = []
    def __init__(self, lista = []):
        self.__lista = lista
    def crearLista(self):
        band = False
        archi = open('ArchivoLibros.csv')
        reader = csv.reader(archi, delimiter = ';')
        for fila in reader:
            if(band == False):
                fila[0] = fila[0][3:]
                if(re.match('^[0-9]', fila[0].lower())):
                    unLibro =claseLibro(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
                    unLibro.crearListaCap(reader)
                    self.__lista.append(unLibro)
                band = True
            else:
                if(re.match('^[0-9]', fila[0].lower())):
                    unLibro = claseLibro(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
                    unLibro.crearListaCap(reader)
                    self.__lista.append(unLibro)
    def punto1(self, id):
        acum = 0
        i = 0
        #buscar el libro en la lista
        while(i<len(self.__lista)):
            if (id == self.__lista[i].getId()):
                break
            i+=1
        #tarea
        print('|----{}----|'.format(self.__lista[i].getTitulo()))
        for x in range(len(self.__lista[i].getCaps())):
            print('-> {}'.format(self.__lista[i].getCaps()[x].getTitulo()))
            acum += int(self.__lista[i].getCaps()[x].getPags())
        print('Contiene {} páginas'.format(acum))
    def punto2(self, palabra):
        band = [False, False]
        for i in range(len(self.__lista)):  #busca la palabra en el libro
            band[0] = False
            for j in range(len(self.__lista[i].getCaps())): #busca la palabra en los capítulos
                if(palabra in self.__lista[i].getTitulo() and band[0] == False):
                    print('|----{}----|\nAutor: {}'.format(self.__lista[i].getTitulo(), self.__lista[i].getAutor()))
                    band = [True, True] #detecta que la palabra se econtró y que se econtró en el título
                if(palabra in self.__lista[i].getCaps()[j].getTitulo()):
                    print('|----{}----|\nAutor: {}'.format(self.__lista[i].getCaps()[j].getTitulo(),
                                                           self.__lista[i].getAutor()))
                    band[1] = True  #detecta que la palabra se econtró
        if(band[1] == False):
            print('ERROR: palabra no encontrada')
    def mostrar(self):
        for i in range(len(self.__lista)):
            self.__lista[i].mostrar()