
import random

options = ["rock", "paper", "scissors"]

user_choice = input("Choose rock, paper, or scissors: ")

while user_choice not in options:
    print("Invalid choice. Please choose again.")
    user_choice = input("Choose rock, paper, or scissors: ")

computer_choice = random.choice(options)

print(f"You chose {user_choice}.")
print(f"The computer chose {computer_choice}.")

if user_choice == computer_choice:
    print("Jeet gya bc!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("Jeet gya bc!")
elif user_choice == "paper" and computer_choice == "rock":
    print("Jeet gya bc!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("Jeet gya bc!")
else:
    print("Haar gya mc.")



# import options = ["+","/","-","*"]    




# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# # Ask user to input the operator
# operator = input("Enter operator (+, -, *, /): ")

# # Perform calculation based on operator
# if operator == "+":
#     result = num1 + num2
# elif operator == "-":
#     result = num1 - num2
# elif operator == "*":
#     result = num1 * num2
# elif operator == "/":
#     result = num1 / num2
# else:
#     print("Invalid operator")

# # Print the result
# print(num1, operator, num2, "=", result)