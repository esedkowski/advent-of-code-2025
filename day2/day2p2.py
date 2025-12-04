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
    half_len = id_len//2
    for i in range(1, half_len+1):
        seq = id_str[:i]
        seq_len = i
        if id_len % seq_len == 0:
            repeating_seq = seq
            for j in range(seq_len, id_len, seq_len):
                if id_str[j:j+seq_len] != seq:
                    repeating_seq = None
                    break
            if repeating_seq != None:
                return False

    return True

def check_id_ranges(file):
    with open(file) as input_file:
        ranges = input_file.read()[:-1].split(",")
    sum = 0
    for id_range in ranges:
        sum += check_id_range(id_range)

    return sum

def test():
    if not is_id_valid(123123124) or is_id_valid(123123123):
        raise ValueError("Id validation error")
    if check_id_ranges(TEST_INPUT_FILE) != 4174379265:
        raise ValueError("Ranges validation error")

def main():
    test()
    print(check_id_ranges(INPUT_FILE))

if __name__ == "__main__":
    main()
