import random


def main():
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    number3 = random.randint(0, 100)
    min_value = number1
    if number2 < min_value:
        min_value = number2
        if number3 < min_value:
            min_value = number3
    print(f'{number1} {number2} {number3}' )
    print(min_value)
    """
    ########################################
    Code Your Program here
    ########################################
    """

    ########################################
    # Do not delete the return statement
    ########################################
    return number1, number2, number3, min_value


if __name__ == '__main__':
    main()
