class Personaje:
    # si defines los atributos dentro del init no necesitas definirlos por fuera
    """nombre = "Default"
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0 """

# puesdes añadir doble guion bajo en los atributos para hacer que no sean accesibles desde afuera
# self es un atributo que hace referencia al objeto y permite accederlo
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep= "")
        print("Fuerza:", self.fuerza)
        print("Inteligencia:", self.inteligencia)
        print("Defensa:", self.defensa)
        print("Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida > 0 #devuelve un valor true o false

    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    # Los getters y setters sirven para acceder y modificar los atributos
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado ", daño, "puntos de daño a ", enemigo.nombre)
        if enemigo.esta_vivo():
            print("La vida de ", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

    # ENCAPSULACIÓN -> como definir la privacidad del método o atributo
    def get_fuerza(self):
        return self.fuerza
    def set_fuerza(self, fuerza):
        if fuerza < 0:
            print("Eror has introducido un valor negativo")
        else:
            self.fuerza = fuerza

    # HERENCIA, como crear una subclase a parte de una clase

class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        #Personaje.__init__(self, nombre, fuerza, inteligencia, defensa, vida) esta es una forma de iniciar la clase padre
        super().__init__(nombre, fuerza, inteligencia, defensa, vida) # esta es otra forma de iniciar los atributos de la clase padre
        self.espada = espada


    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Mata Dragones, daño 10 "))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Número de arma incorrecto")

    # modificar la función atributos dentro de la clase hija

    def atributos(self):
        super().atributos()
        print("Espada:", self.espada)

    def daño(self, enemigo): #modificar eñ daño de la función en la clase hija
        return self.fuerza * self.espada - enemigo.defensa


class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
            super().__init__(nombre, fuerza, inteligencia, defensa, vida)
            self.libro = libro

    def atributos(self):
        super().atributos()
        print("Libro:", self.libro)

    def daño(self, enemigo):  # modificar eñ daño de la función en la clase hija
        return self.inteligencia * self.libro - enemigo.defensa




#guts = Guerrero("Guts", 25, 3, 70, 500, 5)
#vanessa = Mago("Vanessa", 10, 50, 50, 390, 10)
#mi_personaje = Personaje("Bitboss", 10, 1, 5, 100)
#mi_enemigo = Personaje("Enemy Stando", 8, 5, 3, 5)
#mi_personaje.nombre = "BitBoss"
#mi_personaje.fuerza = 10
#print(mi_personaje.nombre)
#print(mi_personaje.fuerza)
#mi_personaje.subir_nivel(1,2,0)
#mi_personaje.atributos()
#print(mi_personaje.esta_vivo())
#mi_personaje.morir()
#print(mi_personaje.atacar(mi_enemigo))
#print(mi_personaje.daño(mi_enemigo))
#print(mi_personaje.vida)
#mi_personaje.atacar(mi_enemigo)
#print(mi_personaje.get_fuerza())
#mi_personaje.set_fuerza(50)
#mi_personaje.atributos()
#guts.atributos()
#guts.cambiar_arma()
#guts.atacar(mi_enemigo)
#vanessa.atributos()
#vanessa.atacar(guts)

#Polimorfismo
personaje_1 = Personaje("Guts", 20, 10, 4, 100)
personaje_2 = Mago("Vanessa", 5, 15, 4, 100, 3)

def combate(jugador_1, jugador_2):
    turno = 1
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", jugador_1.nombre, ":", sep="")
        jugador_1.atacar(jugador_2)
        jugador_2.atacar(jugador_1)
        turno = turno + 1
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)


combate(personaje_1, personaje_2)


