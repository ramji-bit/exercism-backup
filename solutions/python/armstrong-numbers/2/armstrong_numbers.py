"""Determining if the number is armstrong number"""
def is_armstrong_number(number):
    """Determining if the number is armstrong number"""
    str_number = str(number)
    length = len(str_number)
    total_value = 0
    iteration = length
    while iteration > 0:
        total_value = total_value + pow(int(str_number[iteration - 1]), length)
        iteration = iteration - 1
    return total_value == number
