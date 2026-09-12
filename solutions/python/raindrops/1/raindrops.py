"""Number to rain drop"""
def convert(number):
    """
    input:Number
    output: text represent number or number
    """
    result = ''
    flag = False
    if number % 3 == 0:
        result = "Pling"
        flag = True
    if number % 5 == 0:
        result = result + "Plang"
        flag = True
    if number % 7 == 0:
        result = result + "Plong"
        flag = True
    if not flag:
        return str(number)
    return result
    
