def calculate_load(platform):
    total_load = 0
    rows, cols = len(platform), len(platform[0])

    for i in range(rows):
        for j in range(cols):
            if platform[i][j] == 'O': 
                load = rows - i  
                total_load += load

    return total_load

def tilt_platform_north(platform):
    return [''.join(row[::-1]) for row in platform[::-1]]


platform_example = [
    "O....#....",
    "O.OO#....#",
    ".....##...",
    "OO.#O....O",
    ".O.....O#.",
    "O.#..O.#.#",
    "..O..#O..O",
    ".......O..",
    "#....###..",
    "#OO..#....",
]


tilted_platform = tilt_platform_north(platform_example)


total_load = calculate_load(tilted_platform)

print(f"The total load on the north support beams is: {total_load}")
