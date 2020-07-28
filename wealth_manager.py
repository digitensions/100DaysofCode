#!/usr/bin/env python3

import math

"""
This class is going to calculate how many years will it take to generate passive for a given
income from renting apts. Dream script for capitalists...
"""

class Calculator:

    def __init__(self, annual_passive_income, annual_savings, year, price_apartment, annual_renting_income):
        # instance variables necessary for all methods in class. Powerful and usable everywhere within class
        # instance variables that start with '_' means it's a private instance
        # if / else statement removes possibility of float entries for 'year' variable
        if isinstance(year, int):
            self._annual_passive_income = annual_passive_income
            self._annual_savings = annual_savings
            self._year = year
            self._years_needed = year
            self._price_apartment = price_apartment
            self._annual_renting_income = annual_renting_income
            self._answer = {}   # dictionary assigned to _answer necessary for collection of data in test
            self._calculate()   # a private method to call multiple tests with
        else:
            raise TypeError("Please input an Integer")

    def _calculate(self):
        apt_number_owned = 0    # local variables, only usable in private method, _calculate method
        income_reached = 0
        while self._annual_passive_income >= (apt_number_owned * self._annual_renting_income):
            # while loop will stop when desired passive income is equal to or less than the calculated income
            # from money available, how many apartments can be bought? Eg, for 10.4 'frac' stores .4, 'whole' stores 10.
            frac, whole = math.modf((self._annual_savings + income_reached) / self._price_apartment)
            # how many apartments can be bought?
            if whole >= 2:
                apt_number_owned += whole
                # Buy >= two apartments and add to variable
                income_reached = (self._annual_savings + income_reached) - (whole * self._price_apartment)
                # update income_reached variable by deducting purchases from total savings
                income_reached += (apt_number_owned * self._annual_renting_income)
                # update again with additional renting profits for established and new apartments
            elif whole >= 1:
                apt_number_owned += whole
                income_reached = frac * self._price_apartment
                # use the fraction to calculate the monetary value based on apartment price
                income_reached += (apt_number_owned * self._annual_renting_income)
            else:
                income_reached += self._annual_savings

            self._answer[self._year] = [apt_number_owned, round(income_reached)] # populates dictionary key 'year'
            self._year += 1         # ensures final year is incremented but negatively impacts sum in line 60 (- 1 needed)

    def get_results(self):
        return self._answer         # dictionary entry, eg {2019: [1, 66666]}

    def get_years_needed(self):
        return (self._year - 1) - self._years_needed  # '- 1' necessary to counter line 54 += 1 (see note)

    def get_apartments_needed(self):
        key = max(self._answer, key=int)    # 2033
        value = self._answer[key]           # [23.0, 169904]
        number_of_apartments = value[0]     # 23
        return number_of_apartments

    def get_net_worth(self):
        return self.get_apartments_needed() * self._price_apartment # calls method above, then times 23 * price_apartm.

    def print_results(self):
        for k, v in self._answer.items():
            print("Year number: {0}, Apt number owned {1} Passive income ${2}".format(k, v[0], round(v[1])))
        print("You can reach a passive income of ${0}, in {1} years".format(self._annual_passive_income, self.get_years_needed()))

calculator_obj_one = Calculator(15000, 5000, 2020, 80000, 6666)
calculator_obj_one.print_results()
