### Costs modelling section ###

# Modelling major expenses based on their main determining factors.
# Assume they do not change year on year for now.
# N.b. here I define cost as something that negatively impacts my overall real wealth.
# I find this definition more useful than a short term cashflow type distinction,
# since I work under the assumption that I will have the wealth to meet short term
# financial commitments.

def model_housing_costs(years, rent):
    return [rent*12 for i in range(years)]
                
def model_living_costs(years):
    return [6000 for i in range(years)]

def model_costs(years, rent):
    housing_costs = model_housing_costs(years, rent)
    living_costs = model_living_costs(years)
    return [a+b for (a,b) in zip(housing_costs, living_costs)]