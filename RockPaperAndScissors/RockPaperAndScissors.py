from random import randint
import os

d = {1 : "Rock",2 : "Paper", 3 : "Scissors" }
def resultado(usuario, maquina):
    if usuario == 1:
        if maquina == 2:
            return 2, f"{d[maquina]} wins {d[usuario]}"
        elif maquina == 3:
            return 1, f"{d[usuario]} wins {d[maquina]}"
    elif usuario == 2:
        if maquina == 3:
            return 2, f"{d[maquina]} wins {d[usuario]}"
        elif maquina == 1:
            return 1, f"{d[usuario]} wins {d[maquina]}"
    elif usuario == 3:
        if maquina == 2:
            return 2, f"{d[maquina]} wins {d[usuario]}"
        elif maquina == 1:
            return 1, f"{d[usuario]} wins {d[maquina]}"
    return 0, "It's a draw"

print("Hello!\nWelcome to my Rock, Paper or Scissors\n")
play = input("Do you want to play?\nPlease enter y/n:\t").lower()
CpuWins = 0
PlayerWins = 0
GamesPlayed = 0

while play not in ["y", "n"]:
    play = input("Please enter y or n:\t").lower()
os.system("clear") 

while not play == "n":
    eleccion = 0
    while eleccion not in [1,2,3]:
        eleccion = int(input("Choose one of them:\n1) Rock\n2) Paper\n3) Scissors\nSelect:\t"))
        os.system("clear")
    MachineElection = randint(1,3)
    print(f"You choose {d[eleccion]}")
    print(f"The machine choose {d[MachineElection]}")
    punto, resultado_final = resultado(eleccion, MachineElection)
    print(resultado_final)
    if punto == 1:
      PlayerWins += 1
      print("The player wins this play")
    elif punto == 2:
      CpuWins += 1
      print("The machine wins this play")
    GamesPlayed += 1
    print("\n\n")
    print(f"Games played: {GamesPlayed}\nThe player wins: {PlayerWins}\nThe machine wins: {CpuWins}")
    print("\n\n")
    play = input("Do you want to play a new game?\nPlease enter y/n:\t").lower()
    while play not in ["y", "n"]:
        play = input("Please enter y or n:\t").lower()
    os.system("clear") 

print(f"The final stats are:\n\nGames played: {GamesPlayed}\nThe player wins: {PlayerWins}\nThe machine wins: {CpuWins}")
print("\n")
if PlayerWins > CpuWins:
	print(f"The player wins for {PlayerWins-CpuWins} plays")
elif CpuWins> PlayerWins:
	print(f"The machine wins for {CpuWins-PlayerWins} plays")
else:
	print("The player and the machine tied during the game")

print("\nThanks you for playing.\nGOOD BYE!")
