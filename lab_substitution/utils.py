import math


# returns greatest number of range with a gcd equals to 1
def get_greatest_number_of_range(lower_bound: int, upper_bound: int) -> int:
    for number in reversed(range(upper_bound)):
        if number < lower_bound:
            return lower_bound
        if math.gcd(number, upper_bound) == 1:
            return number
