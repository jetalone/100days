print ("Welcome to the tip calculator\n")
total = float(input ("What was the total bill? $"))
percentage = int(input ("What percentage tip would you like to give? 10, 12, or 15? "))
percentage /= 100
num = int(input ("How many people to split the bill? "))
result = round((total + (total * percentage))/num, 2)
result = "{:.2f}".format(result)

print (f"Each person should pay: ${result}") 