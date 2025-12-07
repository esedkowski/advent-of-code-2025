INPUT_FILE = "input"
TEST_INPUT_FILE = "test_input"

def import_data(file):
    ranges = []
    ids = []
    with open(file) as data:
        for line in data:
            if line == f"\n":
                break
            start, end = line[:-1].split("-")
            ranges.append((int(start), int(end)))

        for line in data:
            ids.append(int(line))

    return ranges, ids

def sort_ranges(ranges):
    num_of_ranges = len(ranges)
    if num_of_ranges < 2:
        return ranges

    half_of_ranges = num_of_ranges // 2
    half1 = sort_ranges(ranges[:half_of_ranges])
    half2 = sort_ranges(ranges[half_of_ranges:])

    sorted_ranges = []
    while len(half1) > 0 and len(half2) > 0:
        if half1[0][1] < half2[0][1]:
            sorted_ranges.append(half1.pop(0))
        else:
            sorted_ranges.append(half2.pop(0))
    for i in range(len(half1)):
        sorted_ranges.append(half1.pop(0))
    for i in range(len(half2)):
        sorted_ranges.append(half2.pop(0))

    return(sorted_ranges)

def merge_ranges(sorted_ranges):
    merged_ranges = []
    old_range = ()
    while len(sorted_ranges) > 0:
        if len(old_range) == 0:
            old_range = sorted_ranges.pop()
        else:
            new_range = sorted_ranges.pop()
            if new_range[1] < old_range[0]:
                merged_ranges.append(old_range)
                old_range = new_range
            else:
                old_range = (min(old_range[0], new_range[0]), max(old_range[1], new_range[1]))

    merged_ranges.append(old_range)

    return merged_ranges




def check_ids(ranges, ids):
    count = 0
    for id in ids:
        for start, end in ranges:
            if start <= id <= end:
                count += 1
                break

    return count

def count_fresh_id(ranges):
    count = 0
    for start, end in ranges:
        count += end - start + 1
    return count

file = TEST_INPUT_FILE
file = INPUT_FILE

ranges, ids = import_data(file)
sorted = sort_ranges(ranges)
# print(sorted)
merged = merge_ranges(sorted)
# print(merged)
count = check_ids(merged, ids)
print(count)
count = count_fresh_id(merged)
print(count)
