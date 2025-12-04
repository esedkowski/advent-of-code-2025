INPUT_FILE = "input"
STARTING_POSITION = 50

def split_movement(movement):
    direction = movement[0]
    value = int(movement[1:])
    return direction, value

def move_dial(current_position, direction, value):
    passing_0_count = 0
    full_rotations = value // 100
    passing_0_count = full_rotations
    value = value % 100
    direction_value = 1
    if direction == "L":
        direction_value = -1
    new_position = current_position + direction_value * value
    if new_position > 99 or new_position < 0:
        if new_position < 0:
            direction = 1
        else:
            direction = -1
        new_position = new_position + direction * 100
        if new_position != 0 and current_position != 0:
            passing_0_count += 1

    return new_position, passing_0_count

def count_0s(instructions, starting_position):
    end_at_0_count  = 0
    all_0s_passed = 0
    current_position = starting_position
    for instruction in instructions:
        direction, value = split_movement(instruction)
        current_position, passing_0_count = move_dial(current_position, direction, value)
        if current_position == 0:
            end_at_0_count += 1
        all_0s_passed += passing_0_count
    all_0s_count = end_at_0_count + all_0s_passed

    return all_0s_count, end_at_0_count, all_0s_passed

with open(INPUT_FILE) as input:
    print(count_0s(input, STARTING_POSITION))
