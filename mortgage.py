
class Mortgage:

    def __init__(self, CurrentAccount, deposit_value, initial_loan_value, repayment_term, monthly_payments, fixed_rate, fixed_rate_period):
        self.AssetValue = deposit_value + initial_loan_value
        self.CurrentAccount = CurrentAccount
        self.loan_value = initial_loan_value
        self.years_remaining = repayment_term
        self.monthly_payments = monthly_payments
        self.fixed_rate = fixed_rate
        self.fixed_rate_period_remaining = fixed_rate_period
        self.repayed = False

        self.CurrentAccount.withdraw(deposit_value)

    def get_interest_rate(self):
        if self.fixed_rate_period_remaining > 0:
            self.fixed_rate_period_remaining -= 1
            return self.fixed_rate
        # This can be a potential area for expansion, but for now we'll assume
        # the rate will rise by 1% and stay there.
        return self.fixed_rate + 0.01

    def compound_interest(self):
        self.loan_value *= 1+self.get_interest_rate()
        return self.loan_value

    '''
    This function will execute 12 monthly payments at once on the mortgage.
    If, on a given iteration, this brings us over the total value of the loan,
    it will mark the loan as having been repayed, and will return the amount
    to be rebated.

    Returns: the amount paid in
    '''
    def make_yearly_repayment(self):
        yearly_payments = self.monthly_payments * 12
        if yearly_payments > self.loan_value:
            self.CurrentAccount.withdraw(self.loan_value)
            final_loan_value = self.loan_value
            self.loan_value = 0
            self.repayed = True
            return final_loan_value
        self.loan_value -= yearly_payments
        self.CurrentAccount.withdraw(yearly_payments)
        return yearly_payments
