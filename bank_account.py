
class BankAccount:

    def __init__(self, value, interest_rate):
        self.value = value
        self.interest_rate = interest_rate

    def compound_interest(self):
        self.value *= 1 + self.interest_rate
        return self.value

    def pay_in(self, amount):
        self.value += amount
        return self.value

    def withdraw(self, amount):
        if amount > self.value:
            raise Exception(f'Withdrawing {amount} from an account with balance: {self.value}')
        self.value -= amount
        return self.value