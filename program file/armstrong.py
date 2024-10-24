def is_armstrong_number(number):
    digits = str(number)
    num_digits = len(digits)
    total = 0
    for digit in digits:
        total += int(digit) ** num_digits
    return total == number
number = int(input("Enter a number to check if it is an Armstrong number: "))
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")



                                                     