class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, accName):
        self.balance = initialAmount
        self.name = accName
        print(
            f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")

    def withdrawal(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw Complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdrawal interupted: {error}')

    def transfer(self, amount, account):
        try:
            print('\n*******\n\nBegining Transfer..')
            self.viableTransaction(amount)
            self.withdrawal(amount)
            account.deposit(amount)
            print('\nTransfer complete!\n\n*******')
        except BalanceException as error:
            print(f'\nTransfer interrupted: {error}\n\n*******')


class IntrestRewardAccount(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.getBalance()


class SavingsAccount(IntrestRewardAccount):
    def __init__(self, initialAmount, accName):
        super().__init__(initialAmount, accName)
        self.fee = 5

        def withdrawal(self, amount):
            try:
                self.viableTransaction(amount+self.fee)
                self.balance = self.balance - (amount + self.fee)
                print("\nWithdraw completed.")
                self.getBalance()
            except BalanceException as error:
                print(f'\nWithdrawal Interrupted: {error}')
