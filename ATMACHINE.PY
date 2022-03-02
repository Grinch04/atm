import pandas as pd
class ATM:
    def __init__(self):
        print("Welcome to GRINCH BANK")
    def login(self):
        chance=0
        while chance <3:
            password=input("Enter Password")
            if password==pa:
                print(f"Welcome {na}")
                return True
            else:
                print("Wrong Password")
                chance+=1
        print("Too many incorrect attempts, could not log in")
        return False
    def transfer(self):
        transfer=input("Input amount to transfer: ")
        if int(transfer)<int(ba):
            new_bal=int(ba)-int(transfer)
            print(f'your new balance is :{new_bal}')
            return True
        else:
            print("Insufficient fund available")
            return False
    def withdrawal(self):
        withdrawal=input("Input amount to withdraw: ")
        if int(withdrawal)<int(ba):
            new_bal=int(ba)-int(withdrawal)
            print(f'your new balance is :{new_bal}')
            return True
        else:
            print("Insufficient fund available")
            return False
    def balance_check(self):
        print(ba)
    def  make_transaction(self):
        if self.login()==True:
            print("Press 1 for transfer")
            print("Press 2 for withdrawal")
            print("press 3 for balance checking")
            choice=int(input("What would you like to do: "))
            if choice==1:
                self.transfer()
            elif choice==2:
                self.withdrawal()
            elif choice==3:
                self.balance_check()
            else:
                print("would you like to try again: ")
            return choice
atm=pd.read_excel("C:\\Users\\GRINCH\\Desktop\\MYCODES\\ATM_RECORD.xlsx")
pa=atm.iloc[0]['ACCTPAS']
na=atm.loc[0]['ACCTNAME']
ba=atm.loc[0]['ACCTBAL']
d=ATM()
d.make_transaction()
print("Thank you for banking with us")
            
            