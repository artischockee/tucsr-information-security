import math


def lcm(a, b) -> int:
    return a * b / math.gcd(a, b)


def are_integers_coprime(int_1: int, int_2: int) -> bool:
    return math.gcd(int_1, int_2) == 1


def get_coprime_integer(upper_bound: int) -> int:
    for i in range(2, upper_bound):
        if are_integers_coprime(i, upper_bound):
            return i
    return 1
