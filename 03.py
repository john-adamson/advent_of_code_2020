"""
Advent of Code 2020: Day 03.
"""

SLOPE = [
    '...#..............#.#....#..#..',
    '...#..#..#..............#..#...',
    '....#.#.......#............#...',
    '..##.....##.........#........##',
    '...#...........#...##.#...#.##.',
    '..#.#...#....#.....#........#..',
    '....##.###.....#..#.......#....',
    '.#..##...#.....#......#..#.....',
    '............##.#...#.#.....#.#.',
    '..........#....#....#.#...#...#',
    '..##....#.#.#......#.........#.',
    '#.#.........#..............##..',
    '....##.##......................',
    '....##..#...........#..........',
    '..#..#.#........##....#......#.',
    '..............#..#....#.....#..',
    '.............#...#.....#...#...',
    '.#...........#..........#...#..',
    '.#......#.......#......#.......',
    '#..#.............#..#....##.###',
    '........#.#...........##.#...#.',
    '......#..#.....##......#.......',
    '.....#.....#....#..............',
    '#...##.#......#......#...#.....',
    '...........................#...',
    '...#....................#.....#',
    '..#.....#...#.....##.....#.....',
    '....................#......#..#',
    '.......#.....##......##....#...',
    '#........##...#.....##..#...#..',
    '........#..#.#......#..###..#.#',
    '##.....#.............#.#....#..',
    '..#.................#....######',
    '.#.#..#.....#.#..........#.#...',
    '.........#....#...#............',
    '........#..#.....#.............',
    '............#.#.............##.',
    '...#....#..#......#............',
    '.##....#.....#...#.#...........',
    '..#..............#...........##',
    '.....#.#.##...#................',
    '..........#..#.#..........##..#',
    '..#....#...#...#.....######....',
    '....#.#..#........#....#.###...',
    '.......................#.......',
    '..#.....#.##................#..',
    '.....#......#..#.....#........#',
    '.#...###.......#.#.........#..#',
    '............#..................',
    '..#.........##.........##......',
    '#...........#.#.......###.#....',
    '.#...#.....#.........###.....#.',
    '.#............#........#..#....',
    '...##.#......##................',
    '........#...#...#...#..........',
    '.......#.##......##.#..........',
    '....##.......#..#....#....#....',
    '......#.........###........#...',
    '#....#....####....##......#....',
    '......................#....#.#.',
    '...#.#.#....#.#...#...#......#.',
    '......#.....##.#...........###.',
    '#........#.........##......#.#.',
    '....##.....#.....#..#..........',
    '......#...#...#.........#...##.',
    '..#........#..................#',
    '.........#..##.#..#..#...#.#..#',
    '.....#.....#...#.....###.....##',
    '.............#....#...#........',
    '..........#.#.#...#..#...#....#',
    '#...............##.......#.....',
    '#...#.............#..#...#....#',
    '..#...#...##...##...#..#.......',
    '..#..#........#.#...........#..',
    '.....#.....#..................#',
    '....#....##....###..###...##...',
    '..#......###.........##....#.##',
    '.......#.##...#.......#..#.....',
    '...#.#.#.#.....##..#..#........',
    '................##....#.#......',
    '..#...#...#...#.....##.#...#..#',
    '..#..#.....#..##....#....#.....',
    '.###...#......#........#.....##',
    '##......#..#........#..........',
    '....#...#..#....##..#......####',
    '.#.....##....#..........#......',
    '.#...#....#.........#...#....#.',
    '.....#..#.#..#......#..##....#.',
    '...#.##...#...#........#......#',
    '.#..#...#.#..#.........#...#...',
    '#....#......##.....#.......#...',
    '..##............##..#.#.#...#..',
    '##.......#.......##............',
    '#......#.##........#...#...#...',
    '.#.#.......##.........#..#.#...',
    '.............##.#........#.....',
    '.#..#...###...#..#.............',
    '.....#...#..#....#.......#.....',
    '#.#.........#.#.#...#...#.#....',
    '.....#.......#.##.##...#....#..',
    '.#.##..#.....#...#.#.#.#.#..#..',
    '..........#...................#',
    '.....#.#.#...##.........#..#..#',
    '.#..#....##......#...#.........',
    '.##......#......#...#........#.',
    '.....##.#......#............#.#',
    '.#.....##..#...........##......',
    '.....#......#.......##....#....',
    '..#..##..........#.#..........#',
    '#.#.......##..#..##.#....#.....',
    '.......#..#.#.......##......#.#',
    '....#...##...#..............#..',
    '.....#.........#......#...##...',
    '#.........#........##..#.....#.',
    '.#.#..#.....##.......#......#..',
    '........#..#....#.....###..#...',
    '#.#..#.#..........#............',
    '..#......##..#....#.........#..',
    '#..............................',
    '.......#............#..#..#.#..',
    '.#.....#.#....#..#.##.#........',
    '.......#.###.#........##.#..#..',
    '..............#....#.....##.#..',
    '#..............#....#.###......',
    '.#..#..#...###............#...#',
    '.#.##...#....#..#...#...#......',
    '......##..#..#......#..#....#..',
    '.........#.......##............',
    '...........##...#..#....####...',
    '.#..................#..........',
    '#...#..#..................#....',
    '..............#.....##.....#...',
    '..#.#..#...##..#.....#.....#..#',
    '....#....#.#.........#.....#...',
    '.#.......#...#....#...#.#..#..#',
    '#.........##.....##.......#...#',
    '#..#............#....#........#',
    '..........##...#......#....#...',
    '.......#..##...............#...',
    '#............#.#.#.....#.......',
    '.#........##...#...............',
    '..##....#.....#..#.##.#......#.',
    '.#...#.............#...#.....#.',
    '...##....#.......#......#.#..#.',
    '#......................#..#.##.',
    '...#..........#..#.........#...',
    '..#......#.......#.#....#......',
    '....#............#...#......#..',
    '.....#..#..##...#...#.........#',
    '.....#......#....#....#........',
    '.............#..#..........#...',
    '....#..............#.....#.#...',
    '....#.................#.#...#.#',
    '.........#.#...........###.#.##',
    '#...........#..##.#....#.##.#..',
    '#.#.....#......................',
    '##.#.........#....##.#.#..#.#..',
    '#..........#.#.#.#.#..#..##..#.',
    '..#...#..###.........#......#..',
    '.....#......#..#.#............#',
    '...........#...#.#.#.###....#..',
    '#....#..#.......##.#.......##..',
    '..............#.....##.#.......',
    '.#.....#.#..#.........#.#.#..#.',
    '..#..#..#..#................#..',
    '...........#..#.#...#.........#',
    '.#..#..#...#........#...#.#..#.',
    '...#.#..#......#..#............',
    '........#......##.....#....#...',
    '#...#......##.#.#..............',
    '.#........................#....',
    '#.#.....#.##.....#..#.#........',
    '#..........##.#.......#....#..#',
    '#...#..#..#.....#....#....#....',
    '#...........#..#.#....##.##....',
    '##......#..#........#.......##.',
    '#........#..#...#..........#...',
    '...#...#......##....#.#........',
    '...##..#..#.##....#...#........',
    '#.#..#....#...#........#.......',
    '..........#.......#..........#.',
    '......##...#....###...#....#...',
    '........#..#.....#......#......',
    '....#.........##...#..##......#',
    '....#...........#.#..#.#.#.#..#',
    '..#......#..#......#........#.#',
    '#..#....#.....#.............#..',
    '............................#..',
    '#...#.#.....#...#....#....#....',
    '........#...#...#...#...#......',
    '.###........#....#.##.....##.#.',
    '.........#.....#..........#....',
    '.#.........#....##.#.....#.....',
    '#..#....................##.#...',
    '..##.#.............#....#.#....',
    '..#.#........#............##.#.',
    '#........#...##.....#...#.....#',
    '.........#.#..........#....#..#',
    '...###.#..#.#......#.#.....#...',
    '......#.....#..#...#........#..',
    '.......#...#.....#....#....#..#',
    '.#.#........#......##.......#..',
    '#.................###..........',
    '#........#.#..#....#..#........',
    '..##....#.#...##...#...##....#.',
    '...#.#......##...#.....#..#....',
    '#..#........#...###....#.......',
    '##.#....#..#.#..........#......',
    '....#...###...#.....#........#.',
    '..#.#........#....##.#.........',
    '......##.##.................##.',
    '.#....##...#.#..#.#............',
    '.#...###........#......#.......',
    '##..#.#......#..#..#...#.......',
    '.......##..#....#........#....#',
    '......#..........#.............',
    '....##..##..#......#.#.........',
    '.....#....................##...',
    '...###.....#.....#...#.#.##.#..',
    '....#.#..#.......#..#......##..',
    '.......#.#..#.##.#...#......#..',
    '...#.#....#.#...#..##...#...#..',
    '#.##...#....#..#.............#.',
    '...#...#...#.......#..........#',
    '.#..#.............#..##.#......',
    '....#.......#..............#.#.',
    '..................#..#.....##.#',
    '.#...#..#......#..........#...#',
    '..#.#.....#..#....#....#####.#.',
    '.......###.......#....#....#...',
    '......#.#........#...#.........',
    '......#..#.#.#....#.#.#....##..',
    '.#...#.#...##.#......#.........',
    '#....#..##....#.#.......#....#.',
    '..##.#.....#.....#.........#...',
    '......#......#....#....#.....#.',
    '...##.....#....#......#......#.',
    '......#......##............#.#.',
    '.##.#.......#....#...#....#....',
    '....#..#..#...##.......#..#....',
    '....#....#...#.#........#..#...',
    '....#.....#..........#..#......',
    '....#....#...#.....#..##.....#.',
    '##...#..##......#....##..#..#..',
    '.....##.##..............##.....',
    '#.#....#.##..#....#...##.......',
    '..#.....##.....#.....######...#',
    '...#.....#.#.#......#......##.#',
    '...........##.............#....',
    '...##......#..#......#...#.....',
    '....#.##......#..#....#.#..#...',
    '.#..#....#...#..#.....##.......',
    '.....#..#.................#..#.',
    '................#..#...#......#',
    '...##....#.....#..#....##......',
    '....##...............##...#....',
    '......#..........#..##.........',
    '.......###.......#.........#..#',
    '......................#....#.#.',
    '#.#.....#...##............#....',
    '........#......##......#.....#.',
    '...#....#....#.#..##.#..#.#.#..',
    '..#.#....#.##...#..#.....#.#...',
    '............#....#..#.......#..',
    '#...#...#.#......#...##.....#.#',
    '......#....#....#.......#......',
    '....#.......#..........#....#..',
    '........#####........#....#....',
    '......#....##..............#.#.',
    '....#....#.......#.......#.....',
    '.##.#....##....#...............',
    '#.....##........#..#.#...#.#...',
    '...#......##....#..............',
    '.#.....#.....#.......##....##..',
    '#....#..........#.#..#.........',
    '......##..........##.......#...',
    '.##......##.....#.#....#......#',
    '....#......................#...',
    '.#...........###........#...#..',
    '#.#..#..#..#...##.#....#.#..#..',
    '...##...........#.#..........#.',
    '......#.#..#....#....#.........',
    '....#....#.#......#.........##.',
    '.#..#...#...##....#...#......#.',
    '#.#......#...#.#.#...........#.',
    '##.....#..........##....##..##.',
    '...#.#.....#..##........#......',
    '..#........##........#..#......',
    '.......#...............##..#...',
    '.......#.#....#..###...........',
    '.............#........#...#....',
    '#.................#......#..#..',
    '...#....#..#..............#...#',
    '.............#....##....#..##..',
    '#........#..........##...##...#',
    '............#....#.....#.#....#',
    '.....#..............##..#...#..',
    '..#....#......###....#.#...##..',
    '....##......#.....#....#.......',
    '.....#...............#.....#...',
    '.#.....#.....#..............#..',
    '#................#..#..........',
    '.##....#....#.....#............',
    '#.####...#..#..#....#..........',
    '..##........##.....##......#..#',
    '......#.....#...##.........##..',
    '....##..#.....#.#.........#...#',
    '.....##..#....#....#.#...#..#..',
    '...#............#...........#..',
    '.......#.#..#.#.#..#........#.#',
    '....#.#........#.#.#..#...#...#',
    '..#....#....#..#......#........',
    '.#...........................#.',
    '.#..#....####........##......#.',
    '.#.....#..#.#.................#',
    '.#..#...........#...#....#...#.',
    '......##..#........#..#....#...',
    '..#.............#....#........#',
    '#.#..........#.##.......#.#..#.',
    '..#....#...#...............#...',
    '..............#..........#..#..',
    '..#.....#.#.....#...#...#..#...',
    '.........#...###.#...#........#',
]

TRAJECTORIES = [
    {'right': 1, 'down': 1},
    {'right': 3, 'down': 1},
    {'right': 5, 'down': 1},
    {'right': 7, 'down': 1},
    {'right': 1, 'down': 2}
]


def tree_count(right, down):
    count, column = 0, 0
    for row in range(0, height, down):
        # Use a column wrap.
        if SLOPE[row][column % width] == '#':
            count += 1
        # Advance the column.
        column += right
    return count


if __name__ == '__main__':

    height = len(SLOPE)
    # Assumes:
    #   1) There is at least one row.
    #   2) All rows are the same length.
    width = len(SLOPE[0])

    # Part 1:
    print(f'Part 1: {tree_count(right=3, down=1)}')

    # Part 2:
    product = 1
    for trajectory in TRAJECTORIES:
        product *= tree_count(right=trajectory['right'],
                              down=trajectory['down']
                              )
    print(f'Part 2: {product}')
