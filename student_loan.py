from tax_modelling import *

class StudentLoan:

    def __init__(self, CurrentAccount, initial_loan_value, repayment_bands, repayment_rates):
        self.CurrentAccount = CurrentAccount
        self.loan_value = initial_loan_value
        self.repayment_bands = repayment_bands
        self.repayment_rates = repayment_rates
        self.repayed = False

    def get_interest_rate(self, salary):
        lower_threshold = 27295
        upper_threshold = 49130
        lower_interest_rate = 0.026
        upper_interest_rate = 0.056
        if salary < lower_threshold:
            return lower_interest_rate
        if salary > upper_threshold:
            return upper_interest_rate
        gradient = (upper_interest_rate-lower_interest_rate)/(upper_threshold-lower_threshold)
        return gradient*salary + lower_interest_rate

    def compound_interest(self, salary):
        self.loan_value *= 1+self.get_interest_rate(salary)
        return self.loan_value

    def get_minimum_repayment(self, salary):
        # The structure of the student loan is perfectly analagous to a tax,
        # so we can reuse this method from our tax modelling script
        return get_tax_from_bands(salary, self.repayment_bands, self.repayment_rates)

    def make_repayment(self, amount):
        # If the loan is fully paid off mark it as such
        if amount >= self.loan_value:
            self.CurrentAccount.withdraw(self.loan_value)
            final_value = self.loan_value
            self.loan_value = 0
            self.repayed = True
            return final_value
        # Otherwise subtract the balance due
        self.loan_value -= amount
        self.CurrentAccount.withdraw(amount)
        return amount

    def make_minimum_repayment(self, salary):
        curr_loan_value = self.loan_value
        min_repayment = self.get_minimum_repayment(salary)
        return self.make_repayment(min_repayment)

    def pay_off_in_full(self):
        self.make_repayment(self.loan_value)
