#!/usr/bin/env python3

#filename apimon.py

# imports always go at the top of your code
import requests

def main():
        
    try:
        userSel = input("Please enter a Pokemon name: ")
    
        pokeapi = requests.get("https://pokeapi.co/api/v2/pokemon/"+userSel.lower()).json()
        numGames = 0
        moveNum = 0

        for element in pokeapi:
            if element == "sprites":
                for pic in pokeapi[element]:
                    if pic == "front_default":
                        print("A picture of " + userSel + " can be found at " + pokeapi[element][pic])

            if element == "game_indices":
                for game in pokeapi[element]:
                    numGames = numGames+1

            if element == "moves":
                for moveInd in pokeapi[element]:
                    for moveTitle in pokeapi[element][moveNum]:
                        if moveTitle == "move":
                            print(pokeapi[element][moveNum][moveTitle]["name"])
                    moveNum = moveNum + 1

        print(userSel+ " has appeared in " + str(numGames) + " games!")
        #print(pokeapi)
    
    except:
        print("That is not a Pokemon!")

main()
