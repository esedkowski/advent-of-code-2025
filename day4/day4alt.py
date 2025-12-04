import copy
import time

INPUT_FILE = "input"
TEST_INPUT_FILE = "test_input"

def convert(_input):
    grid = []
    for row in _input:
        new_row = []
        for character in row[:-1]:
            if character == "@":
                new_row.append(1)
            else:
                new_row.append(0)
        grid.append(new_row)

    return grid

def count_and_remove(grid):
    num_of_rows = len(grid)
    num_of_col = len(grid[0])
    count = 0
    old_count = -1
    while old_count != count:
        old_count = count
        for row in range(num_of_rows):
            for col in range(num_of_col):
                loc_count = 0
                if grid[row][col] == 1:
                    for i in range(-1,2):
                        for j in range(-1,2):
                            if not row + i < 0 and not row + i > num_of_rows - 1 and not col + j < 0 and not col + j > num_of_col - 1 and not (i == 0 and j == 0):
                                if grid[row + i][col + j] == 1:
                                    loc_count += 1
                    if loc_count < 4:
                        count += 1
                        grid[row][col] = 0

    return count

file = INPUT_FILE

t0 = time.perf_counter()
with open(file) as _input:
    grid = convert(_input)

print(count_and_remove(grid))
t1 = time.perf_counter()
print(f"{t1 - t0:0.4f} seconds")
