def is_prime_list(numbers):
    for num in numbers:
        if (num <= 1):
            return 'error'
        if ( num > 1):
            for n in range(2, num):
                if num % n == 0:
                    return "is n\'t Prime numbers"
        else:
            return False
    return 'is Prime numbers'