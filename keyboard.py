import command_line

#  Returns a list of numbers given by the user
# INPUT: none
# OUTPUT: list[float] representing given numbers
def gather_numbers() -> list[float]:
    numbers = []
    repeat = "T"
    while repeat == "T":
        user_input = input("Enter a number: ")
        num = convert.str_to_float(user_input)
        numbers.append(num)
        repeat = input("Would you like to enter another number? [T/F]: ")
    return numbers

if __name__ == '__main__':
    numbers = gather_numbers()
    print(sum(numbers))







