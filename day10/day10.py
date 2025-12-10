import re
import time

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
            joltages_str = re.findall(r"\d", joltage_str)
            for j in joltages_str:
                joltage.append(int(j))

            machines.append((lights, buttons, joltage))

        return machines

def find_combination(state, goal, b_sets, limit, count=0, steps=[]):
    count += 1
    if count == limit or len(b_sets) == 0:
        # print("limit", steps)
        return limit
    num_of_sets = len(b_sets)
    for i in range(num_of_sets):
        new_steps = steps.copy()
        temp_state = state.copy()
        b_set = b_sets[i]
        for b in b_set:
            temp_state[b] = (temp_state[b] + 1) % 2
        if temp_state == goal:
            # print("goal:", steps)
            return count

        new_steps.append(b_set)
        # print(temp_state, goal, b_sets[:i] + b_sets[i+1:], limit, count, new_steps)
        new_count = find_combination(temp_state, goal, b_sets[i+1:], limit, count, new_steps)
        if new_count < limit:
            limit = new_count

    return limit

def get_fewest_presses(machine):
    lights_input = machine[0]
    b_sets = machine[1]

    lights = []
    for char in lights_input:
        if char == ".":
            lights.append(0)
        else:
            lights.append(1)

    num_of_lights = len(lights)

    state = [0] * num_of_lights
    # print(state, lights, b_sets, len(b_sets))
    count = find_combination(state, lights, b_sets, len(b_sets))

    return count

machines = get_input(file)
# print(machines)

result = 0
count = 0
t0 = time.perf_counter()
for machine in machines:
    count += 1
    result += get_fewest_presses(machine)
print(result)
t1 = time.perf_counter()
print(f"{t1 - t0:0.4f} seconds")
