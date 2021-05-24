from Menu import claseMenu
import os
def test():
    pass
if __name__ == '__main__':
    if(input('¿Testear?: ').lower() == 'si'):
        test()
    else:
        #variables
        band = False
        menu = claseMenu()
        #tareas
        menu.menu(0)
        while not band:
            print('|----MENU----|\n1. Buscar libro\n2. Buscar palabra\n3. Salir')
            op = int(input('Opción: '))
            os.system('cls')
            menu.menu(op)
            band = op == 3