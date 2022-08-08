def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        test("FizzBuzz")
        test = True 
    elif number % 3 == 0:
        print("Fizz")
        test = True 
    elif number % 5 == 0:
        print("Buzz")
        test = True
    else:  
        test = False
    return test 