for number in range(1,100):
    if number % 3 == 0 and number % 5 == 0:
        print(f"{number} is fizzbuzz")
    elif number % 3 == 0:
        print(f"{number} is fizz")
    elif number % 5 == 0:
        print(f"{number} is buzz")
    else:
        print(number)            