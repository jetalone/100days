print("Welcome to the tip calculator.")

total = input("What was the total bill? $")
perc= input("What percentage tip would you like to give? ")
num = input("How many people to split the bill? ")

nperc = (int(perc)/100) + 1
ntot = (float(nperc) * float(total))/float(num)
rtot = round(ntot,2)

print(f"Each person should pay: ${rtot}")