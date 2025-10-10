class AtmWallet:
    def __init__(self,amount=0):
        self.__amount = amount  # Private
        self.__pin = "1234"    # Private
        self.currency = 'bitcoin'

    def check_balance(self, pin):
        if pin == self.__pin:
            return self.__amount
        else:
            ValueError = "Invalid PIN"

    def deposit(self, amount, pin):
        if amount <=0:
            ValueError = 'Deposit amount must be positive'

        if amount >0:
            print('amount deposited successfully:',self.__amount)   
            
        if pin == self.__pin:
            print ('pin matched correctly')
            self.__amount += amount
            
        else:
            print('amount deposited successfully:',self.__amount,self.currency)    
        
     


        
akram=AtmWallet()
akram.deposit(10000,"1234")

print('akram has deposited:',akram.check_balance("1234"),akram.currency)



class Hello:
    def __init__(self,names):
        self.a = 10
        self._B= 20
        self.__c = 30
hello = Hello("name")
print(hello.a)
print(hello._B) #protected
#print(hello.__c) #private