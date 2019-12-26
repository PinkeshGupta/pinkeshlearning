import random

list1=["s","w","g"]

chance= 10
noc=0
com_point =0
player_point =0

print("Snake \t Water \t Gun Game")
print("s for snake \n w for water \n g for gun")

while noc < chance:
    u_input =input("Please select yout choice snake , water or Gun \n")
    c_input =random.choice(list1)


    if u_input == c_input:
        print("Game is tie 0 point to each")

    if u_input == "s" and c_input=="g":
        com_point = com_point +1 
        print(f"Your input is {u_input} and computer input is {c_input}\n")
        print("Computer win and get 1 point \n")
        print(f"your points is {player_point} and compputer points is {com_point}")

    elif u_input == "s" and c_input=="w":
        player_point = player_point +1 
        print(f"Your input is {u_input} and computer input is {c_input}\n")
        print("Player win and get 1 point \n")
        print(f"your points is{player_point} and compputer points is {com_point}")

    elif u_input == "w" and c_input=="s":
        com_point = com_point +1 
        print(f"Your input is {u_input} and computer input is {c_input}\n")
        print("Computer win and get 1 point \n")
        print(f"your points is{player_point} and compputer points is {com_point}")

    elif u_input == "w" and c_input=="g":
        player_point = player_point +1 
        print(f"Your input is {u_input} and computer input is {c_input}\n")
        print("Player win and get 1 point \n")
        print(f"your points is{player_point} and compputer points is {com_point}")

    elif u_input == "g" and c_input=="s":
        com_point = com_point +1 
        print(f"Your input is {u_input} and computer input is {c_input}\n")
        print("Computer win and get 1 point \n")
        print(f"your points is {player_point} and compputer points is {com_point}")

    elif u_input == "g" and c_input=="w":
        player_point = player_point +1 
        print(f"Your input is {u_input} and computer input is {c_input}\n")
        print("Player win and get 1 point \n")
        print(f"your points is {player_point} and compputer points is {com_point}")

    else:
        print(f"{u_input} this is invalid input")

    noc = noc +1
    print(f"{chance-noc} is left out {chance}")

print("Game Over")

if com_point > player_point:
    print("computer is winner")
if player_point > com_point:
    print("User is winner ")

print(f"point of player is {player_point} and point of computer is {com_point}")





