from replit import clear

# Addition
def add(n1,n2):
  return n1+n2

# Substract
def substract(n1,n2):
  return n1-n2

# Multiply
def multiply(n1,n2):
  return n1*n2

# Division
def division(n1,n2):
  return n1/n2

operations = {
  "+":add,
  "-":substract,
  "*":multiply,
  "/":division
}

def calculator():
  num1 = float(input("What's the first number?: "))
  
  for symbol in operations:
    print(symbol)
  should_continue = True

  while should_continue:
    operation_symbol = input("Pick one operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1,num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start new.:") == "y":
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()
calculator()
