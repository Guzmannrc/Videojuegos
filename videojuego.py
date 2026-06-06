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

        letra = input("Ingresa una letra: ").lower()
    
        if letra not in self.letras_adivinadas:
            self.letras_adivinadas.append(letra)
        else:
            print("Ya ingresaste esa letra")

    def verificar_ganador(self):

        for letra in self.palabra:

            if letra not in self.letras_adivinadas:
                return False
        return True

    def pedir_letra(self):

        letra=input("Ingresa una letra:").lower()
        
        if letra not in self.letras_adivinadas:
            self.letras_adivinadas.append(letra)
            
            if letra not in self.palabra:
                self.intentos -= 1
                print("Letra incorrecta")
                print("Intentos resrantes:",self.intentos)
        else:
            print("Ya ingresaste esa letra")

    def verificar_perdedor(self):
        return self.intentos <=0

juego = VideojuegoAhorcado()

while True:

    juego.mostrar_palabra()

    juego.pedir_letra()

    if juego.verificar_ganador():

        print("Bn hecho!")
        print("La palabra era:", juego.palabra)
        break

    if juego.verificar_perdedor():

        print("Bot!")
        print("La palabra era:", juego.palabra)
        break


