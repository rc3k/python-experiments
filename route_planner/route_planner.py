def possible_next_steps(row, column, map_matrix):
    possibilities = []
    if row < len(map_matrix) - 1:
        possibilities.append((row + 1, column))
    if row > 0:
        possibilities.append((row - 1, column))
    if column < len(map_matrix[row]) - 1:
        possibilities.append((row, column + 1))
    if column > 0:
        possibilities.append((row, column - 1))
    return [p for p in possibilities if map_matrix[p[0]][p[1]]]


def find_next_steps(positions, map_matrix, already_seen):
    next_steps = [next_step for p in positions for next_step in possible_next_steps(p[0], p[1], map_matrix)]
    return [n for n in next_steps if n not in already_seen]


def route_exists(from_row, from_column, to_row, to_column, map_matrix):
    positions = [(from_row, from_column)]
    already_seen = set([(from_row, from_column)])
    while len(positions):
        positions = find_next_steps(positions, map_matrix, already_seen)
        if any([p == (to_row, to_column) for p in positions]):
            return True
        already_seen |= set(positions)
    return False


if __name__ == '__main__':
    map_matrix = [
        [True, True, False, False],
        [True, True, True, False],
        [False, False, True, True],
        [False, False, True, False],
    ]

    print(route_exists(0, 0, 2, 3, map_matrix))
