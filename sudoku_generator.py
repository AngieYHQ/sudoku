import random
import copy

def is_valid(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    box_start_row, box_start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[box_start_row + i][box_start_col + j] == num:
                return False
    return True

def solve(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

def generate_full_solution():
    grid = [[0] * 9 for _ in range(9)]
    fill_grid(grid)
    return grid

def fill_grid(grid):
    nums = list(range(1, 10))
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                random.shuffle(nums)
                for num in nums:
                    if is_valid(grid, i, j, num):
                        grid[i][j] = num
                        if solve(copy.deepcopy(grid)):
                            return True
                        grid[i][j] = 0
                return False
    return True

def remove_numbers(grid, difficulty):
    level_map = {
        'Easy': 35,
        'Medium': 45,
        'Hard': 55
    }
    puzzle = copy.deepcopy(grid)
    cells_to_remove = level_map.get(difficulty, 45)
    attempts = 0
    while cells_to_remove > 0 and attempts < 1000:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if puzzle[row][col] != 0:
            backup = puzzle[row][col]
            puzzle[row][col] = 0
            copy_grid = copy.deepcopy(puzzle)
            if solve(copy_grid):
                cells_to_remove -= 1
            else:
                puzzle[row][col] = backup
        attempts += 1
    return puzzle
