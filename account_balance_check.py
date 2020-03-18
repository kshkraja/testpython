

class Account:
    
    def __init__(self,accbal):
        
        self.accbal=accbal
    def withdraw(self,amnt):
        if self.accbal-amnt>1000:
            self.accbal = self.accbal - amnt
    def deposit(self,amnt):
        self.accbal = self.accbal + amnt

if __name__=='__main__':
    accbal = 10000
    a = Account(accbal)
    amnt = 1000
    a.withdraw(amnt)
    a.deposit(100)
    print("after withdraw and deposit {}".format(a.accbal))
    
        
