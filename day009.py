from replit import clear

print ( '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
print ("Welcome to the secret auction!")
bidders= {}
bidlist = []
gameover= False
yn = False
while gameover==False:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))
    bidders[name] = bid
    while yn == False:
        others = input("Are there other users who want to bid? (yes/no) ").lower()
        if others == "no" or others == "n":
            gameover = True
            break
        elif others == "yes" or others == "y":
            clear()
            break
        else:
            print("Invalid input. Try again.")


key_list = list(bidders.keys())
val_list = list((bidders.values()))

high = max(val_list)


position = val_list.index(high)
winner = (key_list[position])

print (f"The winner is {winner} with a bid of ${high}.")