# Welcoming message
print("\n")
print("======================================================")
welcome = '----------WELCOME TO THE BANK OF THE PEOPLE----------'
print(welcome)
print("======================================================" + "\n")

# Creating account pin/password
password = input("Enter your password to login to your account.\n")
print("Your PIN is successfully created\n")

# Initial deposit/funding
total_amount = input("Enter amount to create account.\n")

# Command prompt for more transcation
nMessage = int(input("Enter 1 for check your balance.\nEnter 2 for deposite.\nEnter 3 for withdrawal.\nEnter 4 for transfer.\n"))

pin = input("Enter your PIN\n")


if(pin==password):

    # Case 1
    if(nMessage == 1):
        print("Your balance is " + total_amount)

    # Case 2
    elif(nMessage == 2):
        deposite = input("Enter amount to deposite\n")
        sum = int(total_amount)+int(deposite)
        print("Net Balance after Deposite is", sum)

    # Case 3
    elif(nMessage == 3):
        withdraw = input("Enter amount to withdraw\n")
        minus = int(total_amount)-int(withdraw)
        print("Net Balance after Withdraw is", minus)

    # Case 3
    elif(nMessage == 4):
        transfer = input("Enter amount to transfer\n")
        details = input("Enter Beneficiary Account Number\n")
        tran = int(total_amount)-int(transfer)
        print("You transferred",transfer,"to",details)
        print("Net Balance after Transfer is", tran)
    
    else:
        print("Enter a valid user input")
        
    
else:
    print("Your password is wrong repeat the process again")
