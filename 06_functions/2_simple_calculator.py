def add(a, b):
    return a + b
 
def sub(a, b):
    return a - b
 
def mul(a, b):
    return a * b
 
def div(a, b):
    return a / b
 
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
 
choice = int(input("Enter your choice (1-4): "))
 
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
 
if choice == 1:
    print("Result =", add(x, y))
 
elif choice == 2:
    print("Result =", sub(x, y))
 
elif choice == 3:
    print("Result =", mul(x, y))
 
elif choice == 4:
    if y == 0:
        print("Error: Cannot divide by zero")
    else:
        print("Result =", div(x, y))
 
else:
    print("Invalid Choice")