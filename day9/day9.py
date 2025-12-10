INPUT = "input"
TEST_INPUT = "test_input"

file = TEST_INPUT
# file = INPUT

def get_data(file):
    tiles = []
    with open(file) as _input:
        for line in _input:
            x, y = line.split(",")
            tiles.append((int(x),int(y)))

    return tiles

def abs(number):
    return number if number > 0 else number * (-1)

def find_biggest_square(tiles):
    num_of_tiles = len(tiles)
    biggest_area = 0
    for i in range(num_of_tiles):
        for j in range(i + 1, num_of_tiles):
            p1 = tiles[i]
            p2 = tiles[j]
            area = (abs(p2[0] - p1[0]) + 1) * (abs(p2[1] - p1[1]) + 1) # +1 to handle 'of by 1 error'
            if area > biggest_area:
                biggest_area = area
                biggest_square = (p1, p2, biggest_area)

    return biggest_square

tiles = get_data(file)
biggest_square = find_biggest_square(tiles)
print(biggest_square[2])
