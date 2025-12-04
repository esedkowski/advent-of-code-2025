import copy
import time

INPUT_FILE = "input"
TEST_INPUT_FILE = "test_input"

# with open(file) as banks:

def count_horizontal_neighbours(row, is_previous_roll=0):
    for position in row:
        if position == "@":
            is_roll = 1
        else:
            is_roll = 0
        if len(row) > 1:
            new_row = count_horizontal_neighbours(row[1:], is_roll)
            is_next_roll = new_row[0][0]
        else:
            is_next_roll, new_row = 0, []

        horizontal_neighbours = is_previous_roll + is_next_roll
        new_row.insert(0, [is_roll, horizontal_neighbours])

        return new_row

def count_neighbours(_input):
    rows = []
    for row in _input:
        horizontal_neighbours = count_horizontal_neighbours(row[:-1])
        rows.append(horizontal_neighbours)

    new_grid = copy.deepcopy(rows)
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if i > 0:
                upper_neighbours = sum(rows[i-1][j])
            else:
                upper_neighbours = 0
            if i < len(rows) - 1:
                lower_neighbours = sum(rows[i+1][j])
            else:
                lower_neighbours = 0
            new_grid[i][j][1] = upper_neighbours + rows[i][j][1] + lower_neighbours

    return new_grid

def count_removable(grid):
    num_of_rows = len(grid)
    num_of_col = len(grid[0])
    counter = 0
    to_be_removed = []

    while True:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j][0] == 1 and grid[i][j][1] < 4:
                    to_be_removed.append([i, j])
        counter += len(to_be_removed)
        if len(to_be_removed) == 0:
            break
        while len(to_be_removed) > 0:
            row, column = to_be_removed.pop()
            grid[row][column][0] = 0
            for i in range(-1,2):
                for j in range(-1,2):
                    if not row + i < 0 and not row + i > num_of_rows - 1 and not column + j < 0 and not column + j > num_of_col - 1 and not (i == 0 and j == 0):
                        grid[row + i][column + j][1] -= 1

    return counter

file = INPUT_FILE
t0 = time.perf_counter()
with open(file) as _input:
    counted_neighbours = count_neighbours(_input)

print(count_removable(counted_neighbours))

t1 = time.perf_counter()
print(f"{t1 - t0:0.4f} seconds")
