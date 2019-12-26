import sys
class customer:

    Bankname ="GUPTA BANK"
    def __init__(self,name,balance=0):
        self.name =name
        self.balance =balance

    def deposit(self,amt):
        self.balance =self.balance +amt
        print(f"Amount after deposit is {self.balance}")
    
    def withdraw(self,amt):
        if amt > self.balance:
            print("Insufficent amount in account !")
            sys.exit()
        self.balance =self.balance -amt
        print(f"Amount after withdraw is {self.balance}")

chance = 3
noc = 0
print(f"Welcome to {customer.Bankname}")
name =input("Please  enter your name: ")
c=customer(name)
# while noc < chance:
while noc<chance:
    print("Please select operation \n D: Deposit \n W: Withdraw \n E: Exit ")
    option =input("Select any one from above \n")
    if option=="D" or option =="d":
        amt=float(input("Please enter the amount to deposit: "))
        c.deposit(amt)           
    elif option=="W" or option=="w" :
        amt=float(input("Please enter the amount you want to withdraw: "))
        c.withdraw(amt)
    elif option=="E" or option=="e":
        print("Thanks for banking with us")
        sys.exit()
    else:
        print("Please choose valid option ")
    noc = noc + 1
    
        
print("Login again for banking with us")
sys.exit()        

       
        
     

       
  
        