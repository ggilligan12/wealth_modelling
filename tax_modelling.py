# Helper methods to calculate tax

'''
Given a salary and an interval, tell us how much of the salary falls in that interval

int - salary: salary in consideration
int - band_start: the lower end of this interval
int - band_end: the lower end of this interval
'''
def get_salary_in_band(salary, band_start, band_end):
    if salary > band_end:
        return band_end - band_start
    if salary < band_start:
        return 0
    return salary - band_start

'''
Given the lower threshold of tax bands, and the rate of tax in those bands as lists,
we can calculate the total tax owed on some amount of salary.

int - salary: salary we want to determine the tax on
list<int> - band_lower_limits: the lower limit of the tax band we're considering
list<float> - band_rates: the fraction of income in this band that is forfeit

nb. band_lower_limits[0] must always be 0
'''
def get_tax_from_bands(salary, band_lower_limits, band_rates):
    tax_total = 0
    for i in range(len(band_lower_limits)-1):
        sib = get_salary_in_band(salary, band_lower_limits[i], band_lower_limits[i+1])
        tax_total += sib * band_rates[i]
    # In all tax systems there is a highest rate where all further income off to infinity
    # is taxed at that rate, we must add that on at the end
    salary_in_top_band = get_salary_in_band(salary, band_lower_limits[-1], 9999999999)
    tax_total += salary_in_top_band * band_rates[-1]
    return tax_total

'''
Given the bands and rates for the two major taxes UK citizens are subject to,
we calculate the total tax owed on a given salary.

int - salary: salary we want to determine the total tax on
list<int> - ni_bands_lower_limits: the lower limits of National Insurance bands
list<float> - ni_rates: the rate of taxation in each NI band
list<int> - it_bands_lower_limits: the lower limit of Income Tax bands
list<float> - it_rates: the rate of taxation in each Income Tax band
'''
def get_tax(salary, ni_bands_lower_limits, ni_rates, it_bands_lower_limits, it_rates):
    # National insurance
    ni = get_tax_from_bands(salary, ni_bands_lower_limits, ni_rates)
    # Income tax
    it = get_tax_from_bands(salary, it_bands_lower_limits, it_rates)
    # Total tax deducted
    return ni + it
