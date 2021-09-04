from art import calclogo

def add(n1, n2):
  return n1 + n2
def sub(n1, n2):
  return n1 - n2
def mul(n1, n2):
  return n1 * n2
def div(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": sub,
  "*": mul,
  "/": div,
}

print(calclogo)
def calculate():
  
  num1 = float(input("What's the first number? "))

  for symbol in operations:
    print(symbol)

  should_continue = True

  while should_continue:
    operation_symbol = input("Choose an operation from above: ")
    num2 = float(input("What's the next number? "))
    answer = operations[operation_symbol](num1, num2)
    print (f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer} or 'n' to start a new calculation: ") == "y":
      num1 = answer
    else:
      should_continue = False
      calculate()
      
calculate()