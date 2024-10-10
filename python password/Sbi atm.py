# write a program to program and create a ATM machine


A=("Welcome to SBI ATM ")
print(A.center(100))
balance=5000
PIN=int(input("Enter your PIN "))

if PIN == 1234:
    print("1.Balance check ")
    print("2.withdraw money ")
    print("2.Deposit Money ")
    option=int(input("specify what you want to perfom :"))
    if option == 1:
        print("your current balance is ",balance)
    elif option == 2:
            amount = int(input("Enter the amount you want to withdraw: "))
            if amount>balance:
                print("Insufficient funds! ")
            else:
                    balance-=amount
                    print("withdrawel Successful. Your new balance is ",balance)
    elif option ==3:
            amount = int(input("enter the amount to deposit :"))
            balance+=amount
            print("Deposit sucessful . Your new balance is ", balance)
    else:
                print("invalid option selected")
else: print("incorrect pin.please try again")