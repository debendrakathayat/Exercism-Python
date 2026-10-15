def is_armstrong_number(number):
    copy = number
    sum = 0
    power = len(str(number))
    while copy > 0:
        remainder = copy % 10
        sum += remainder ** power 
        copy //= 10
    return sum == number
        
