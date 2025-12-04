INPUT_FILE = "input"
TEST_INPUT_FILE = "test_input"

def check_id_range(id_range):
    invalid_ids_sum = 0
    start, end = id_range.split("-")
    start_int, end_int = int(start), int(end)
    for current_id in range(start_int, end_int+1):
        if not is_id_valid(current_id):
            invalid_ids_sum += current_id

    return invalid_ids_sum

def is_id_valid(id):
    id_str = str(id)
    id_len = len(id_str)
    if id_len % 2 == 0:
        half_len = int(id_len / 2)
        first_half = id_str[0:half_len]
        second_half = id_str[half_len:]
        if first_half == second_half:
            return False
    return True

def check_id_ranges(file):
    with open(file) as input_file:
        ranges = input_file.read()[:-1].split(",")
    sum = 0
    for id_range in ranges:
        sum += check_id_range(id_range)

    return sum

if check_id_ranges(TEST_INPUT_FILE) != 1227775554:
    raise ValueError("Test output invalid")

print(check_id_ranges(INPUT_FILE))
