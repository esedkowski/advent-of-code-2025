# technically should work, but gets too long to finish for given input
TEST_INPUT = "test_input"
INPUT = "input"

file = TEST_INPUT
# file = INPUT

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

def get_splits(data, x):
    splits = []
    grid_with = len(data[0])
    old_ray = [x]
    count = 0
    for line in data:
        ray = []
        for x in old_ray:
            if line[x] == "^":
                count += 1
                if not x-1 in ray: # skipping <0 check, because there is at least one space of pading in input data
                    ray.append(x-1)
                if not x+1 in ray:
                    ray.append(x+1)
            else:
                if not x in ray:
                    ray.append(x)
        old_ray = ray.copy()

    return count

data = get_data(file)
x = get_start(data)
splits = get_splits(data[0:], x)
# print(splits)
print(splits)
