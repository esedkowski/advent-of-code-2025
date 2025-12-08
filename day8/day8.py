import re
import math

INPUT = "input"
TEST_INPUT = "test_input"

file = TEST_INPUT
file = INPUT

def get_points(file):
    with open(file) as _input:
        points = []
        for line in _input:
            x, y, z = re.findall(r"\d+", line)
            points.append((int(x), int(y), int(z)))

    return points

def calculate_distance(p1, p2):
    sum = 0
    for i in range(len(p1)):
        sum += (p1[i] - p2[i]) ** 2
    distance = math.sqrt(sum)

    return distance


def get_distances(points):
    num_of_points = len(points)
    distances = []
    for i in range(num_of_points):
        point1 = points[i]
        for j in range(i + 1, num_of_points):
            point2 = points[j]
            distance = calculate_distance(point1, point2)
            distances.append((i, j, distance))

    return distances

def sort_distances(distances):
    num_of_distances = len(distances)
    if num_of_distances < 2:
        return distances

    half_of_distances = num_of_distances // 2
    half1 = sort_distances(distances[:half_of_distances])
    half2 = sort_distances(distances[half_of_distances:])

    sorted_distances = []
    while len(half1) > 0 and len(half2) > 0:
        if half1[0][2] < half2[0][2]:
            sorted_distances.append(half1.pop(0))
        else:
            sorted_distances.append(half2.pop(0))
    for i in range(len(half1)):
        sorted_distances.append(half1.pop(0))
    for i in range(len(half2)):
        sorted_distances.append(half2.pop(0))

    return(sorted_distances)

def make_circuits(distances):
    circuits = []
    for distance in distances:
        extended_circuits = []
        for circuit in circuits:
            if distance[0] in circuit and distance[1] in circuit:
                extended_circuits.append(circuit)
                break
            elif distance[0] in circuit:
                circuit.append(distance[1])
                extended_circuits.append(circuit)
            elif distance[1] in circuit:
                circuit.append(distance[0])
                extended_circuits.append(circuit)
            else:
                pass
        if len(extended_circuits) == 0:
            circuits.append([distance[0], distance[1]])
        elif len(extended_circuits) == 1:
            pass
        else:
            c1 = extended_circuits.pop()
            c2 = extended_circuits.pop()
            circuits.pop(circuits.index(c1))
            circuits.pop(circuits.index(c2))
            new_circuit = list(set(c1+c2))
            circuits.append(new_circuit)
        # print(circuits)
        # input()

    return circuits

def sort_circuits(circuits):
    num_of_circuits = len(circuits)
    if num_of_circuits < 2:
        return circuits

    half_of_circuits = num_of_circuits // 2
    half1 = sort_circuits(circuits[:half_of_circuits])
    half2 = sort_circuits(circuits[half_of_circuits:])

    sorted_circuits = []
    while len(half1) > 0 and len(half2) > 0:
        if len(half1[0]) > len(half2[0]):
            sorted_circuits.append(half1.pop(0))
        else:
            sorted_circuits.append(half2.pop(0))
    for i in range(len(half1)):
        sorted_circuits.append(half1.pop(0))
    for i in range(len(half2)):
        sorted_circuits.append(half2.pop(0))

    return(sorted_circuits)

def result(sorted_cir, num):
    product = 1
    biggest_cir = sorted_cir[:num]
    for circuit in biggest_cir:
        product *= len(circuit)
    return product

points = get_points(file)
print(points[:3])
distances = get_distances(points)
print(distances[:3])
if file == INPUT:
    sorted_dist = sort_distances(distances)[:1000]
else:
    sorted_dist = sort_distances(distances)[:10]
print(sorted_dist[:5])

circuits = make_circuits(sorted_dist)
print(circuits)

sorted_cir = sort_circuits(circuits)
print(sorted_cir)

print(result(sorted_cir, 3))
