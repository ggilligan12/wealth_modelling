### Salary Modelling ###

def model_salary(years, starting_salary, annual_payrise, bonus_percentage):
    salary = starting_salary
    yearly_salary = [salary*(1+bonus_percentage)]
    for i in range(years-1):
        salary += annual_payrise
        yearly_salary += [salary*(1+bonus_percentage)]
    return yearly_salary
