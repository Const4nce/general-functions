import statsmodels.api as sm
import numpy as np

def population_proportion_test(control_population: int, control_proportion: float,
                               treatment_population: int,
                               treatment_proportion: float, significance_threshold: float = 0.01
                               ):
    population1 = np.random.binomial(1, control_proportion, control_population)
    population2 = np.random.binomial(1, treatment_proportion, treatment_population)
    result = sm.stats.ttest_ind(population1, population2)
    if result[1] < significance_threshold:
        print('There is significant difference between two populations, null hypothesis can be'
              'rejected')
        print(f"Pval: {result[1]}")
    else:
        print('There is no significant difference between two populations')
        print(f"Pval: {result[1]}")


