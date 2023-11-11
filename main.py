print("Welcome to Treasure Island \n your mission is to find treasure")

choie1 = input("which direction you want to go ,left or right : ")

if choie1 == "left":
    print("you have chosen the right door(correct) \n good with next one")
    choie2 = input("you want to choose , swim or wait :")
    if choie2 == "wait":
        print("again , you chosen the right option \n go on")
        choie3 = input("choose one , red,blue or green :")
        if choie3 == "green":
            print(f"you chose {choie3} door and won the whole game \n also you take your treasure")
        else:
            print("finally you lost it ")
    else:
        print("you choose to swim hence sink in river")
else:
    print("you lose")

