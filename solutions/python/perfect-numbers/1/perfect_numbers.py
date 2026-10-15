def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    sum = 0
    count = 1
    while count != number:
        if number % count == 0:
            sum =sum + count;
        count +=1
    if sum == number:
        return "perfect"
    if sum > number:
        return "abundant" 
    if  sum < number:
        return "deficient" 
        
