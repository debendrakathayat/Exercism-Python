def is_armstrong_number(number):
    copy = number
    addition = 0
    power = len(str(number))
    while copy > 0:
        remainder = copy % 10
        addition += remainder ** power 
        copy //= 10
    return addition == number
        
