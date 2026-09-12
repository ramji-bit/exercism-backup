"""Determining if the number is armstrong number"""
def is_armstrong_number(number):
    str_number = str(number)
    length = len(str_number)
    total_value = 0
    i = length
    while i > 0:
        total_value = total_value + pow(int(str_number[i - 1]), length)
        i = i - 1
    return total_value == number
