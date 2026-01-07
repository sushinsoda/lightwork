print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
fork = input("You are walking in a forest, there is a fork in the road. Which do you take - left or right? ")
if fork == "left":
    print("You fall into a hole and break your ankle.")
else:
    print("You walk into a clearing and see a lake with a house at the end")
    lake = input("You see the tide is lowering - do you swim or wait?")
    if lake == "swim":
        print("You get attacked by trout. Game")
    else:
        print("You walk across the lake and make it to the house")
        door = input("You walk up to the house and see 3 doors, which do you choose? red, yellow, blue?")
        if door == "red":
            print("A lit candle falls on the floor and burns everything. You die")
        elif  door == "blue":
            print("Oh no this is where the dogs live. They attack and eat you")
        elif door == "yellow":
            print( "You enter a room with food. You win")
        else:
            print("That is incorrect, you activated booby trap. you die")
print("Game over")
