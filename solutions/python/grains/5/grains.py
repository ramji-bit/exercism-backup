def square(number):
    """
    Returns the square
    """
    if not 64 >= number >= 1:
        raise ValueError("square must be between 1 and 64")
    ans = 1
    while number > 1:
        ans = ans * 2
        number = number - 1
    return ans 

def total():
    """
    Returns the total
    """
    number = 64
    total_value = 0
    while number >= 1:
        total_value = total_value + square(number)
        number = number - 1
    return total_value
