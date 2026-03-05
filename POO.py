class Habitacion:
    def __init__ (self, descripcion = "", norte = 0, sur = 0, este = 0, oeste = 0):

        self.descripcion = descripcion
        self.norte = norte
        self.sur = sur
        self.este = este 
        self.oeste = oeste

if __name__ == '__main__' :

    lista_habitaciones = []

    habitacion_0 = Habitacion()
    habitacion_0.descripcion = "Estas en tu dormitorio, el cuál huele un poco mal, no nos vamos a mentir\nHay habitaciones al este"
    habitacion_0.norte = None
    habitacion_0.sur = None
    habitacion_0.este = 1
    habitacion_0.oeste = None

    lista_habitaciones.append(habitacion_0)

    habitacion_1 = Habitacion()
    habitacion_1.descripcion = "Estas en el pasillo que conecta tu habitación con el salón y con otro pasilo, el cual está un poco oscuro\nHay habitaciones al este, oeste y norte\n En que dirección quieres ir?"
    habitacion_1.norte = 4
    habitacion_1.sur = None
    habitacion_1.este = 2
    habitacion_1.oeste = 0

    lista_habitaciones.append(habitacion_1)

    habitacion_2 = Habitacion()
    habitacion_2.descripcion = "Estas en el salón, donde tu padre está durmiendo y echando unos ronquidos terribles\nHay habitaciones al oeste"
    habitacion_2.norte = None
    habitacion_2.sur = None
    habitacion_2.este = None
    habitacion_2.oeste = 1

    lista_habitaciones.append(habitacion_2)

    habitacion_3 = Habitacion()
    habitacion_3.descripcion = "Estas en la habitación de tus padres, en está tu perro djugando con una pelota encima de las cama de tus padres\nHay habitaciones al este"
    habitacion_3.norte = None
    habitacion_3.sur = None
    habitacion_3.este = 4
    habitacion_3.oeste = None

    lista_habitaciones.append(habitacion_3)

    habitacion_4 = Habitacion()
    habitacion_4.descripcion = "Estas en el pasillo que conecta el pasillo de tu habitación con el balcon y en el que huele la comida que está preparando tu madre\nHay habitaciones al norte, sur, este y oeste"
    habitacion_4.norte = 6
    habitacion_4.sur = 1
    habitacion_4.este = 3
    habitacion_4.oeste = 5

    lista_habitaciones.append(habitacion_4)

    habitacion_5 = Habitacion()
    habitacion_5.descripcion = "Estas en la cocina, donde tu madre está preprando la cena y hay en el ambiente un olor a cebolla terrible\nHay habitaciones al este"
    habitacion_5.norte = None
    habitacion_5.sur = None
    habitacion_5.este = 4
    habitacion_5.oeste = None

    lista_habitaciones.append(habitacion_5)

    habitacion_6 = Habitacion()
    habitacion_6.descripcion = "Estas en el balcon, en el cual corre un fuerte viendo y puedes ver como un niño vuelva una cometa en el parque de en frente\nHay habitaciones al sur"
    habitacion_6.norte = None
    habitacion_6.sur = 4
    habitacion_6.este = None
    habitacion_6.oeste = None

    lista_habitaciones.append(habitacion_6)

    habitacion_actual = 0

    salir = False

    while not salir:
        print()
        print (lista_habitaciones[habitacion_actual].descripcion)
        direccion = input(print("¿En que dirección quieres ir?"))

        if direccion.lower() == 'n' or direccion.lower == 'norte':
            siguiente_habitacion = lista_habitaciones[habitacion_actual].norte
            if siguiente_habitacion == None:
                print("No puedes ir en esa dirección")
            else:
                habitacion_actual = siguiente_habitacion

        elif  direccion.lower() == 's' or direccion.lower == 'sur':
            siguiente_habitacion = lista_habitaciones[habitacion_actual].sur
            if siguiente_habitacion == None:
                print("No puedes ir en esa dirección")
            else:
                habitacion_actual = siguiente_habitacion

        elif direccion.lower() == 'o' or direccion.lower == 'oeste':
            siguiente_habitacion = lista_habitaciones[habitacion_actual].oeste
            if siguiente_habitacion == None:
                print("No puedes ir en esa dirección")
            else:
                habitacion_actual = siguiente_habitacion 

        elif direccion.lower() == 'e' or direccion.lower == 'este':
            siguiente_habitacion = lista_habitaciones[habitacion_actual].este
            if siguiente_habitacion == None:
                print("No puedes ir en esa dirección")
            else:
                habitacion_actual = siguiente_habitacion 
        else: 
            print ("No se ha entendido muy bien hacia donde quieres ir")

        fin = input (print("Indica si quieres salir del juego (si/no): "))
        if fin.lower() == 'no':
            salir = False
        else:
            salir == True
        










