#For this challenge,create a bank account class that has two attributes
class BankAccount: 

    def __init__(self): 

        self.ownerName="RAVI KIRAN"
        
        self.Balance=0
        
    def deposit(self): 
        
        Amount=float(input("\nEnter amount to be Deposited : ")) 
        
        self.Balance += Amount 
        
        print("\nAmount Deposited is :",Amount) 
  
    def withdraw(self): 
        
        Amount = float(input("\nEnter amount to be Withdrawn : ")) 
        
        if self.Balance >= Amount: 
        
            self.Balance -= Amount 
            
            print("\nYou have Withdrew :", Amount) 
        
        else: 
        
            print("\nInsufficient balance in the account...") 

print("\n---WELCOME TO BACK ACCOUNT PROGRAM---")
    
BA = BankAccount()

print("\nAccount Holder Name is :",BA.ownerName)
    
print("\nInitial Account Balance is :",BA.Balance)
   
BA.deposit();
    
BA.withdraw();
    
print("\nNet Avaliable balance is : ",BA.Balance)
