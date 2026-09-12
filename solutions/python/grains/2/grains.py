def square(number):
    if not(number >= 1 and number <=64):
        raise ValueError("square must be between 1 and 64")
    total = 1
    while number > 1:
        total = total * 2
        number = number - 1
    return total 


def total():
    number = 64
    total_value = 0
    while number >= 1:
        total_value = total_value + square(number)
        number = number - 1
    return total_value
