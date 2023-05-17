from random import randint

choices = ["Piedra", "Papel", "Tijera"]

def main():
    player_score = 0
    computer_score = 0
    
    print("Bienvenidos al juego de Piedra, Papel, Tijera!🧮\n")
    
    while True:
        computer = choices[randint(0, 2)]
        player = input("Tu elección...🙃: ").capitalize()

        if player == "Fin":
            print("¡Gracias por jugar🥳!")
            print("Puntaje Final:")
            print(f"Jugador: {player_score}")
            print(f"Computadora: {computer_score}")
            break

        print("Elección de Computadora💻: " + computer)

        if player == computer:
            print("Empate🖍")
        elif player == "Piedra" and computer == "Papel":
            print("¡La computadora gana!🎆")
            computer_score += 1
        elif player == "Piedra" and computer == "Tijera":
            print("¡El jugador gana!🎆")
            player_score += 1
        elif player == "Papel" and computer == "Piedra":
            print("¡El jugador gana!🎆")
            player_score += 1
        elif player == "Papel" and computer == "Tijera":
            print("¡La computadora gana!🎆")
            computer_score += 1
        elif player == "Tijera" and computer  == "Piedra":
            print("¡La computadora gana!🎆")
            computer_score += 1
        elif player == "Tijera" and computer == "Papel":
            print("¡El jugador gana!🎆")
            player_score += 1
        else:
            print("Elección inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
