def fizz_buzz(number):
    if number == 0 :
        test = "Out of Range"
    elif number % 3 == 0 and number % 5 == 0:
        test = 'FizzBuzz'
    elif number % 3 == 0:
        test ='Fizz'
    elif number % 5 == 0:
        test = "Buzz"
    else:
        test = "Out of Range"
    return test 