import random

class VideojuegoAhorcado:

    def __init__(self):

        with open("palabras.txt","r")as archivo:
            self.palabras = archivo.read().splitlines()

        self.__palabra = random.choice(self.palabras)

        self.letras_adivinadas = []

        self.intentos = 5

    def mostrar_palabra(self):

        for letra in self.__palabra:

            if letra in self.letras_adivinadas:
                print(letra, end=" ")

            else:
                print("_", end=" ")

        print()

    def verificar_ganador(self):

        for letra in self.__palabra:

            if letra not in self.letras_adivinadas:
                return False
        return True

    def pedir_letra(self):

        try:
            letra = input("Ingresa una letra: ").lower()

            if len(letra) !=1:
                raise ValueError
            if letra not in self.letras_adivinadas:
                self.letras_adivinadas.append(letra)

                if letra not in self.__palabra:
                    self.intentos -= 1

                    print ("letra incorrecta")
                    print("Intentos restantes:", self.intentos)
            else:
                    print("Ya ingresaste esa letra")

        except ValueError:
            print("Error: Debes ingresar solo una letra. ")

    def verificar_perdedor(self):
        return self.intentos <=0

juego = VideojuegoAhorcado()

while True:

    juego.mostrar_palabra()

    juego.pedir_letra()

    if juego.verificar_ganador():

        print("Bn hecho!")
        print("La palabra era:", juego._VideojuegoAhorcado__palabra)
        break

    if juego.verificar_perdedor():

        print("Bot!")
        print("La palabra era:", juego._VideojuegoAhorcado__palabra)
        break


