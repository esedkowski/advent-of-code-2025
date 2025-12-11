
#   SHOULD WORK, BUT TOO POORLY OPTIMISED 

import re
import time
import copy

file = "test_input"
file = "input"

def get_input(file):
    with open(file) as _input:
        buttons = []
        machines = []
        for line in _input:

            lights = re.search(r"[\.#]+", line)[0]

            buttons = []
            buttons_raw = re.findall(r"\([\d,]+\)", line)
            for buttons_set in buttons_raw:
                new_set = []
                for b in re.findall(r"\d", buttons_set):
                    new_set.append(int(b))
                buttons.append(new_set)

            joltage = []
            joltage_str = re.search(r"\{[\d,]+\}", line)[0]
            joltages_str = re.findall(r"\d+", joltage_str)
            for j in joltages_str:
                joltage.append(int(j))

            machines.append((lights, buttons, joltage))

        return machines

def combine(position, state, goal, b_subset, path=[]):
    if state[position] == goal[position]:
        return [(path, state)], True

    paths = []

    for i in range(len(b_subset)):
        new_path = copy.deepcopy(path)
        new_paths = []
        b = b_subset[i]
        new_state = state.copy()
        overflow = False
        for j in range(len(b)):
            new_state[b[j]] += 1
            if new_state[b[j]] > goal[b[j]]:
                overflow = True

        if not overflow:
            new_path.append(b)
            new_paths, end = combine(position, new_state, goal, b_subset[i:], new_path)
            for _path in new_paths:
                paths.append((_path[0], _path[1]))

            if end:
                break

    return paths, False

def find_combination(state, goal, b_sets):
    num_of_counters = len(goal)
    paths = [([],state)]
    for i in range(num_of_counters):
        b_subset = []
        to_be_removed = []
        new_paths = []
        num_of_sets = len(b_sets)
        for j in range(num_of_sets):
            if i in b_sets[j]:
                to_be_removed.append(j)
        to_be_removed.reverse()
        for k in to_be_removed:
            b_subset.append(b_sets.pop(k))
        for path in paths:
            n_p, _ = combine(i, path[1], goal, b_subset, path[0])
            new_paths += n_p
        paths = []
        for new_path in new_paths:
            paths.append(new_path)

    return paths

def get_fewest_presses(machines):
    result = 0
    licznik = 0
    for machine in machines:
        buttons = machine[1]
        joltage = machine[2]
        state = [0]*len(joltage)
        combinations = find_combination(state, joltage, buttons)
        limit = sum(joltage)
        for combination in combinations:
            count = len(combination[0])
            if count < limit:
                limit = count

        licznik += 1
        progress = 100*(licznik/166)
        print("progress:", progress, "%")
        print(limit)

        result += limit

    return result

# print(combine(0, [0,0,0,0], [3,5,4,7], [[0,2], [0,1]]))
# paths = find_combination([0,0,0,0], [3,5,4,7], [[3], [1,3], [2], [2,3], [0,2], [0,1]])
# limit = sum([3,5,4,7])

""" for path in paths:
    count = len(path[0])
    if count < limit:
        limit = count
print(limit) """

machines = get_input(file)

t0 = time.perf_counter()
result = 0
result += get_fewest_presses(machines)
print(result)
t1 = time.perf_counter()
print(f"{t1 - t0:0.4f} seconds")

