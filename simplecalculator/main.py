# simple calculator
import sys

def add(a,b):
  return a+b

def subtract(a,b):
  return a-b

def multiply(a,b):
  return a*b

def divide(a,b):
  if b != 0:
    return a/b
  else:
      print(f"Error: Division by Zero is not allowed.")

def exit():
  print("Exiting the calculator")
  sys.exit()

  try:
    sys.exit()
  except SystemExit:
    print("Program Exited Successfully")


def main():

  
  while True:

    print("Enter the operation you want to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '5':
      exit()

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
      print(f"Result: {add(num1, num2)}")
    elif choice == '2':
      print(f"Result: {subtract(num1, num2)}")
    elif choice == '3':
      print(f"Result: {multiply(num1, num2)}")
    elif choice == '4':
      print(f"Result: {divide(num1, num2)}")
    else:
      print("Invalid Entry please choose a valid option")
    
main()