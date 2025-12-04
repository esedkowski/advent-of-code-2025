INPUT_FILE = "input"
TEST_INPUT_FILE = "test_input"
NUMBER_OF_DIGIT = 12

def get_voltage_from_bank(bank, num_of_digit, starting_digit=0):
    highest_digit_position = 0
    highest_digit = 0
    last_digit = len(bank) - (num_of_digit - 1) # making space for remaining digit
    for i in range(starting_digit, last_digit):
        if int(bank[i]) > highest_digit:
            highest_digit_position = i
            highest_digit = int(bank[i])

    output = highest_digit * 10**(num_of_digit-1)

    if num_of_digit > 1:
        output += get_voltage_from_bank(bank, num_of_digit-1, highest_digit_position+1)

    return output

def get_voltage(file, number_of_digit):
    output = 0
    with open(file) as banks:
        for bank in banks:
            output += get_voltage_from_bank(bank[:-1], number_of_digit)
    return output

if get_voltage_from_bank("987654321111111", NUMBER_OF_DIGIT) != 987654321111:
    raise ValueError("Test #1 value not valid")

if get_voltage(TEST_INPUT_FILE, NUMBER_OF_DIGIT) != 3121910778619:
    raise ValueError("Test #2 not valid")
print(get_voltage(INPUT_FILE, NUMBER_OF_DIGIT))
