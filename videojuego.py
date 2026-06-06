import random

class VideojuegoAhorcado:

    def __init__(self):

        self.palabras = [
            "futbol",
            "ronaldo",
            "gato",
            "mundial",
            "fifa",
            "computadora"
        ]

        self.palabra = random.choice(self.palabras)

        self.letras_adivinadas = []

        self.intentos = 5

    def mostrar_palabra(self):

        for letra in self.palabra:

            if letra in self.letras_adivinadas:
                print(letra, end=" ")

            else:
                print("_", end=" ")

        print()

    def pedir_letra(self):

        letra= input("Ingresa una letra: ").lower()

        if letra not in self.letras_adivinadas:
            self.letras_adivinadas.append(letra)
        else:
            print("Ya ingresaste esa letra")

juego = VideojuegoAhorcado()

juego.mostrar_palabra()

juego.pedir_letra()

juego.mostrar_palabra()


