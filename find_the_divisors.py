def divisors(integer):
    dividibles = []
    for num in range(2, integer):
        if integer % num == 0:
            dividibles.append(num)
    if len(dividibles) == 0:
        return "{integer} is prime".format(integer=integer)
    return dividibles