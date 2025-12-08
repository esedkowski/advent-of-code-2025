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

def get_splits(data, x):
    splits = []
    grid_with = len(data[0])
    old_ray = [x]
    old_ray_num = [1]
    count = 1
    for line in data:
        ray = []
        ray_num = []
        for i in range(len(old_ray)):
            x = old_ray[i]
            num = old_ray_num[i]
            if line[x] == "^":
                count += num
                if not x-1 in ray: # skipping <0 check, because there is at least one space of pading in input data
                    ray.append(x-1)
                    ray_num.append(num)
                else:
                    ray_num[ray.index(x-1)] += num
                if not x+1 in ray:
                    ray.append(x+1)
                    ray_num.append(num)
                else:
                    ray_num[ray.index(x+1)] += num
            else:
                if not x in ray:
                    ray.append(x)
                    ray_num.append(num)
                else:
                    ray_num[ray.index(x)] += num
        old_ray = ray.copy()
        old_ray_num = ray_num.copy()

    return count

data = get_data(file)
x = get_start(data)
splits = get_splits(data[0:], x)
# print(splits)
print(splits)
