class CreditCard:

    def __init__(self, customer, bank, account, limit):

        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0

    def get_customer(self):

        return self._customer
    
    def get_bank(self):

        return self._bank
    
    def get_account(self):

        return self._account
    
    def get_limit(self):

        return self._limit
    
    def get_balance(self):

        return self._balance
    
    def charge(self, price):

        if price + self._balance > self._limit:
            return False
        else: 
            self._balance += price
            return True
        
    def make_payment(self, amount):
        self._balance -= amount


if __name__ == '__main__':

    wallet = []

    wallet.append(CreditCard('Brian', 'Solution', '2135 1433', 2500))
    wallet.append(CreditCard('Cian', 'Trans-nation', '0135 2334', 3500))
    wallet.append(CreditCard('Karen', 'KCB', '1735 1023', 5000))

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print("Customer = ", wallet[c].get_customer())
        print("Bank = ", wallet[c].get_bank())
        print("Account = ", wallet[c].get_account())
        print("Limit = ", wallet[c].get_limit())
        print("Balance = ", wallet[c].get_balance())
        
        print()
        print()

        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
            print("New balance: ", wallet[c].get_balance())