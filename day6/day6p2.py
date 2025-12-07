import math

INPUT_FILE = "input"
TEST_INPUT_FILE = "test_input"

file = TEST_INPUT_FILE
file = INPUT_FILE

input_data = []
with open(file) as _input:
    for line in _input:
        input_data.append(line[:-1])

num_of_rows = len(input_data)
operations = []
operation = []
for i in range(len(input_data[0]) - 1, -1, -1):
    number = ""
    for j in range(num_of_rows):
        character = input_data[j][i]
        # print(character)
        if character == " ":
            pass
        elif character in ["+", "*"]:
            operation.append(int(number))
            operation.append(character)
            operations.append(operation)
            number = ""
            operation = []
        else:
            number += character
    if not character in ["+", "*"]:
        if number != "":
            operation.append(int(number))

grand_total = 0
for operation in operations:
    operator = operation.pop()
    if operator == "+":
        grand_total += sum(operation)
    else:
        grand_total += math.prod(operation)

print(grand_total)
