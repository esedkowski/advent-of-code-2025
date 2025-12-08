# technically should work, but gets too long to finish for given input
TEST_INPUT = "test_input"
INPUT = "input"

file = TEST_INPUT
file = INPUT

def get_data(file):
    data = []
    with open(file) as input_file:
        for line in input_file:
            data.append(line)
    return data

def get_start(data):
    for x in range(len(data[0])):
        if data[0][x] == "S":
            break
    return x

def get_splits(data, x, start_y):
    splits = []
    for y in range(start_y + 1, len(data)):
        if data[y][x] == "^":
            print(x, y)
            splits.append((x,y))
            new_splits_l = get_splits(data, x - 1, y)
            new_splits_r = get_splits(data, x + 1, y)
            for i in range(len(new_splits_l)):
                if not new_splits_l[i] in splits:
                    splits.append(new_splits_l[i])
            for i in range(len(new_splits_r)):
                if not new_splits_r[i] in splits:
                    splits.append(new_splits_r[i])
            break

    return splits

data = get_data(file)
x = get_start(data)
splits = get_splits(data[], x, 0)
# print(splits)
print(len(splits))
