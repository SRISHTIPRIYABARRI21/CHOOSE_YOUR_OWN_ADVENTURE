name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("you are on a dirt road, it has come to an end and you can go left or right.Which way would u like to go?").lower()

if answer == "left":
    answer = input("you come to a river, you can walk around it or swim across? type walk around and swim to swim accross: ")
    
    if answer == "swim":
            print("you swim across and were eaten by an aligator")
    elif answer == "walk":
            print("you walked for many miles, ran out of water and you lost the game. ")
    else:
            print("Not a valid option. You lose.")
     
elif answer == "right":
    answer = input("you came to a bridge,it looks wobbly, do u want to cross it or head back(cross/back)?")
             
if answer == "back":
        print("You go back and lose.")
elif answer == "cross":
        answer = input("you cross the bridge and meet a stranger.Do you talk to them (yes/no)? ")
if answer == "yes":
                print("You talk to a stranger and they give you gold.")
elif answer == "no":
                print("you ignore the stranger and they are offended and you lose.")
else: 
    print("not a valid option used.")
    
    print("Thank you for trying ", name)

