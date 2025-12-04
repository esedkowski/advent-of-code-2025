INPUT_FILE = "input"
TEST_INPUT_FILE = "test_input"

def get_voltage_from_bank(bank):
    highest_digit_position = 0
    highest_digit = 0
    for i in range(len(bank) - 1):
        if int(bank[i]) > highest_digit:
            highest_digit_position = i
            highest_digit = int(bank[i])

    second_highest_digit_position = 0
    second_highest_digit = 0
    for i in range(highest_digit_position + 1, len(bank)):
        if int(bank[i]) > second_highest_digit:
            second_highest_digit_position = i
            second_highest_digit = int(bank[i])

    output = 10 * highest_digit + second_highest_digit
    return output

def get_voltage(file):
    output = 0
    with open(file) as banks:
        for bank in banks:
            output += get_voltage_from_bank(bank[:-1])
    return output

if get_voltage(TEST_INPUT_FILE) != 357:
    raise ValueError("Test value not valid")
print(get_voltage(INPUT_FILE))
