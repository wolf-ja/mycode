#!/usr/bin/env python3


farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

print("The " + farms[0]["name"] + " has ")


for product in farms[0]["agriculture"]:
    print(product)


runNum=0

while(runNum == 0):
    userFarm = input("Please select a farm from NE Farm, W Farm, or SE Farm: ")
    
    if(userFarm == farms[0]["name"]):
        print("The " + farms[0]["name"] + " has ")

        for product in farms[0]["agriculture"]:
            print(product)
        runNum = 1

    elif(userFarm == farms[1]["name"]):
        print("The " + farms[1]["name"] + " has ")

        for product in farms[1]["agriculture"]:
            print(product)
        runNum = 1
    elif(userFarm == farms[2]["name"]):
        print("The " + farms[2]["name"] + " has ")

        for product in farms[2]["agriculture"]:
            print(product)
        runNum = 1
    else:
        print("That was not a valid farm name, please try again.")

runNum = 0

while(runNum == 0):
    userFarm = input("Please select a farm from NE Farm, W Farm, or SE Farm: ")
    
    if(userFarm == farms[0]["name"]):
        print("The " + farms[0]["name"] + " has ")

        for product in farms[0]["agriculture"]:
            if(product != "sheep" and product != "cows" and product != "pigs" and product != "llamas" and product != "chickens" and product != "llamas" and product != "cats"): 
                print("") 
            else:
                print(product)
        runNum = 1

    elif(userFarm == farms[1]["name"]):
        print("The " + farms[1]["name"] + " has ")

        for product in farms[1]["agriculture"]:
            if(product != "sheep" and product != "cows" and product != "pigs" and product != "llamas" and product != "chickens" and product != "llamas" and product != "cats"):
                print("")
            else:
                print(product)
        runNum = 1

    elif(userFarm == farms[2]["name"]):
        print("The " + farms[2]["name"] + " has ")

        for product in farms[2]["agriculture"]:
            if(product != "sheep" and product != "cows" and product != "pigs" and product != "llamas" and product != "chickens" and product != "llamas" and product != "cats"):
                break
            else:
                print(product)
        runNum = 1

    else:
        print("That was not a valid farm name, please try again.")
