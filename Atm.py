# Try to bulid a mini atm
# pin=1234
# balance=500
# addam=[]
# def add_account():
#     global pin, balance, addam
#     u_pin = int(input("Enter your PIN:"))
#     if u_pin == pin:
#         print("Your current balance is $",balance)
#         print("How much do you want to deposit?")
#         amt = float(input())
#         addam.append(amt)
#         balance += amt
#         print("Deposited successfully! Your new balance is $",balance)

#     else:
#         print("Wrong PIN.")

# def check_balance():
#     global pin,balance,addam
#     print("Your are selected opinion check balance")
#     acc_pin = int(input("Enter your PIN: "))
#     if acc_pin==pin:
#         print("Your balanceis $:",balance)
#     else:
#         return "Invild pin"

# def take_balance():
#     global pin,balance,addam
#     print("Your are selected opinion is withdraws")
#     acc_pin =int(input("Enter your PIN :"))
#     if acc_pin==pin:
#         print("Your current amount:",balance)
#         amt=float(input("Enter a amount:"))
#         if amt<=balance:
#             balance -=amt
#             print("Your acc balance amount:$",balance)
#         else:
#             print("insufficad")
#     else:
#         print("Invalid PIN.")

# # def recepit():
# #     print("Check balance",balance)
# #     print("Add balance",balance)
# #     print("Take balance",a)


# def exit():
#     print("Thank u visit again")
#     exit



# add_account()
# check_balance()
# take_balance()
# # recepit()
# exit()

# class Bank:
#     def __init__(self):
#         self.balance = 0

#     def check_balance(self):
#         print("Your current balance is: ", self.balance)

#     def add_balance(self, amount):
#         self.balance += amount
#         print("You have added: ", amount)

#     def withdraw_cash(self, amount):
#         if amount > self.balance:
#             print("You don't have enough balance!")
#         else:
#             self.balance -= amount
#             print("You have withdrawn: ", amount)

# def main():
#     bank = Bank()

#     menu_options = {
#         "1": bank.check_balance,
#         "2": lambda: bank.add_balance(float(input("Enter amount to add: "))),
#         "3": lambda: bank.withdraw_cash(float(input("Enter amount to withdraw: "))),
#         "4": quit
#     }

#     while True:
#         print("\n1.Check bal\n2.Add_bala\n3.Withdraw cash\n4.Exit")
#         option = input("Enter option number: ")
#         menu_options[option]()

# main()
# a=int(input())
# if a==a:
# print("hi")
# if opt==1:
#                 print("Avalliable Seates:",busc1)
#                 print("Book a seat 1 between 50")
#                 seat=int(input("Enter a Seat  avalible No:"))
#                 if seat <=50:
#                     busc1 -=seat
#                     busbl1.append(seat)
#                     print("The Distance Kms:200 Kms")
#                     print("Rupess:",seat*200*25)
#                     print("Successfully Booked :",seat)
#                     print("Successfully Booked :",busbl1)
#                 else:
#                     print("Please inter 1 bw 50 your entered invaild no")


import time
time.sleep(2)
pin=1234
bal=1000
print("Welcome to Itachi Atm")
time.sleep(3)
print("Insert a  your card")
time.sleep(1)
p=int(input("Enter a Pin:"))
if pin==p:
    time.sleep(1)
    print("Transcation Processing.........")
    while True:
        time.sleep(4)
        print("1.Check Balance\n2.Desopit\n3.Withdrawal")
        opt=int(input("Enter a No:"))
        if opt==1:
            time.sleep(1)
            print("Transcation Processing.........")
            time.sleep(3)
            print("Current balance $",bal)
            time.sleep(2)
            print("Remove your card")
            pass
        elif opt==2:
            print("Transcation Processing.........")
            amt=int(input("Enter a amout to Deposit $"))
            bal +=amt
            time.sleep(1)
            print("Your Desopit amount $",amt)
            time.sleep(1)
            print("Your current balance is $",bal)
            time.sleep(1)
            print("Deposit Successfully ")
            continue



            
        else:
            print("Trascation processing....")
            time.sleep(4)
            print("Invaild pin")
            
else:
    print("Trascation processing....")
    time.sleep(4)
    print("Invaild pin")