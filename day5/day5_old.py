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
            ranges.append([int(start), int(end)])

        for line in data:
            ids.append(int(line))

    return ranges, ids

def sort_ranges(ranges):
    starts = []
    ends = []
    points = []

    for pair in ranges:
        start_inside_other_range = False
        end_inside_other_range = False
        counter_start = 0
        start = pair[0]
        end = pair[1]
        if start == end:
            points.append(start)
            break
        while counter_start < len(starts):
            if start < starts[counter_start]:
                break
            counter_start += 1

        try:
            if counter_start > 0 and start < ends[counter_start - 1]:
                start_inside_other_range = True
        except IndexError:
            pass

        counter_end = len(ends)
        while counter_end > 0:
            if end > ends[counter_end - 1]:
                break
            counter_end -= 1

        try:
            if end > starts[counter_end]:
                end_inside_other_range = True
        except IndexError:
            pass

        if not start_inside_other_range:
            starts.insert(counter_start, start)
            delete_counter =  counter_start + 1
        else:
            delete_counter =  counter_start

        while delete_counter <= len(starts) - 1:
            if starts[delete_counter] < end:
                starts.pop(delete_counter)
            else:
                break

        if not end_inside_other_range:
            ends.insert(counter_end, end)

        delete_counter = counter_end - 1

        while delete_counter >= 0:
            if ends[delete_counter] > start:
                ends.pop(delete_counter)
                delete_counter -= 1
            else:
                break

    for point in points:
        counter = 0
        while counter < len(starts):
            if start < starts[counter]:
                break
            counter += 1
        if counter == 0:
            starts.insert(counter, point)
            ends.insert(counter, point)
        elif counter == len(starts):
            starts.append(point)
            ends.append(point)
        elif point > ends[counter - 1]:
            starts.insert(counter, point)
            ends.insert(counter, point)
        else:
            pass

    return starts, ends

def check_ids(starts, ends, ids):
    count = 0
    for id in ids:
        for i in range(len(starts)):
            if id >= starts[i] and id <= ends[i]:
                count += 1
                break

    return count

ranges, ids = import_data(INPUT_FILE)
starts, ends = sort_ranges(ranges)
print(len(starts), len(ends))
for i in range(len(starts)):
    print(starts[i], ends[i])
count = check_ids(starts, ends, ids)
print(count)
