"""returns number of iterations to reach 1"""
def steps(number):
    """
    returns number of iterations to reach 1
    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    count = 0
    if number == 1:
        return count
    while number > 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = (number * 3) + 1
        count = count + 1
    return count
