from ManejaLibros import claseManejaLibros
class claseMenu:
    __manejador = None
    def __init__(self, manejador = claseManejaLibros()):
        self.__manejador = manejador
    def menu(self, op):
        if(op == 0):    #carga del archivo
            self.__manejador.crearLista()
            print('DATO: el archivo se cargó')
            self.__manejador.mostrar()
            input()
        elif(op == 1):  #buscar lisbro
            self.__manejador.punto1(input('ID del libro: '))
            input()
        elif(op == 2):  #buscar palabra
            self.__manejador.punto2(input('Palabra a buscar: '))
            input()
        elif(op == 3):  #finaliza
            print('DATO: finalizando...')
            input()
        else: print('ERROR: opción inválida')