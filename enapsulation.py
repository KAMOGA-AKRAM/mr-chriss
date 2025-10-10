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
            print('Deposit amount must be positive')
        else:
            print('amount deposited successfully:',self.__amount)
        
        if pin == self.__pin:
            print('pin matched correctly')


        else:
            ValueError = 'invalid pin'
akram=AtmWallet(100)
akram.deposit(10000,"1234")
print(AtmWallet.check_balance)



        