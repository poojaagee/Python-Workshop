#define function calculator  
def calculator(): 
 print("Simple Calculator") 
print("1. Addition") 
print("2. Subtraction") 
print("3. Multiplication") 
print("4. Division") 
#prompt values from user 
choice = int(input("Enter your choice (1-4): ")) 
num1 = float(input("Enter first number: ")) 
num2 = float(input("Enter second number: ")) 
if choice == 1: 
        print("Result:", num1 + num2) 
elif choice == 2: 
        print("Result:", num1 - num2) 
elif choice == 3: 
        print("Result:", num1 * num2) 
elif choice == 4: 
        if num2 != 0: 
            print("Result:", num1 / num2) 
        else: 
            print("Error: Division by zero!") 
else: 
        print("Invalid choice") 
 
#call the function 
calculator() 