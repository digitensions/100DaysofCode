#!/usr/bin/env python3

"""
Coding Challenge Skeleton #4
Two methods that run a sum slightly differently (2 or two 1s) to assess for timing efficiency.
"""

class EfficiencyAdding:

    def adding_two_first_method(self, number_reached):
        while number_reached > 0:
            number_reached -= 2

    def adding_two_second_method(self, number_reached):
        while number_reached > 0:
            number_reached -= 1
            number_reached -= 1
