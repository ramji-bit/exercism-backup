""" Bob's response """
def response(hey_bob):
    """
    Input: Other person's statement to Bob
    Output: Bob's response
    """
    hey_bob = str.rstrip(hey_bob)
    position = -1
    if '?' in hey_bob:
        position = str.index(hey_bob,'?')
    if position == len(hey_bob) - 1 and str.isupper(hey_bob):
        return "Calm down, I know what I'm doing!"
    if position == len(hey_bob) - 1 != -1:
        return "Sure."
    if str.isupper(hey_bob):
        return "Whoa, chill out!"
    if len(hey_bob) < 1:
        return "Fine. Be that way!"
    return "Whatever."
