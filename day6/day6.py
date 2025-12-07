import re
INPUT_FILE = "input"
TEST_INPUT_FILE = "test_input"

file = TEST_INPUT_FILE
file = INPUT_FILE

with open(file) as input_data:
    raw_data = []
    for line in input_data:
        raw_data.append(re.findall(r"\d+|[\+\*]", line))

operators = raw_data.pop()
operations = []
num_of_operations = len(raw_data)
for i in range(len(raw_data[0])):
    operation = [operators[i]]
    for j in range(num_of_operations):
        operation.append(int(raw_data[j][i]))
    operations.append(operation)

grand_total = 0
for operation in operations:
    if operation.pop(0) == "+":
        answer = 0
        for number in operation:
            answer += number
    else:
        answer = 1
        for number in operation:
            answer *= number

    grand_total += answer

print(grand_total)
