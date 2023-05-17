#Lo primero que hacemos es importar el módulo (random) que nos permite generar números aleatorios en Python. 
# Luego, creamos una (lista)llamada (choice) con las opciones del juego: "Piedra", "Papel" y "Tijera".
#................................................................................................................
from random import randint

choice = ["Piedra","Papel","Tijera"]

#Después, definimos la función main(), que es donde se desarrolla el juego
#En esta función, se genera una elección aleatoria para la computadora a través de la función randint()
# Luego, se pide al usuario que introduzca su elección.

def main():
    computer = choice[randint(0,2)]

    print("Bienvenidos al juego de Piedra, Papel y Tijera!\n")
    player = input("Tu elección: ").lower()
    print("Elección de la computadora: " + computer)
    
    
#....................................................................................................................

# A continuación, utilizamos una serie de estructuras if y elif para determinar el ganador del juego.
# Si el jugador y la computadora eligen la misma opción, se imprime "Empate"
# Si la computadora gana, se imprime "La computadora gana!". Si el jugador gana, se imprime "El jugador gana!"
# En caso de que el usuario introduzca "FIN", se termina el juego.

if player == computer:
        print("Empate!")
elif player == "piedra" and computer == "papel":
     print("La computadora gana!")
elif player == "piedra" and computer == "tijera":
     print("El jugador gana!")
elif player == "papel" and computer == "piedra":
    print("El jugador gana!")
elif player == "papel" and computer == "tijera":
     print("La computadora gana!")
elif player == "tijera" and computer  == "piedra":
    print("La computadora gana!")
elif player == "tijera" and computer == "papel":
    print("El jugador gana!")
elif player == "fin":
    print("Gracias por jugar. ¡Hasta la próxima!")
    exit()
#...................................................................................................................

#Luego, dentro de la función main(), se utiliza una variable score para llevar el puntaje de los jugadores
# Si el jugador gana, se le suma un punto al puntaje del jugador
# Si la computadora gana, se le suma un punto al puntaje de la computadora
# En caso de empate, no se suma ningún punto.

    score = {"Jugador": 0, "Computadora": 0}

    if player == computer:
        print("Empate!")
    elif player == "piedra" and computer == "papel":
        print("La computadora gana!")
        score["Computadora"] += 1
    elif player == "piedra" and computer == "tijera":
        print("El jugador gana!")
        score["Jugador"] += 1
    elif player == "papel" and computer == "piedra":
        print("El jugador gana!")
        score["Jugador"] += 1
    elif player == "papel" and computer == "tijera":
        print("La computadora gana!")
        score["Computadora"] += 1
    
