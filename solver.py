"""Main file of the suoku solver."""
import numpy as np
from random import randint


def used_in_row(grid, i, elem):
    """Check that each number on a grid is used exactly once."""
    row = grid[i, :]
    if elem not in row:
        return True
    return False


def used_in_col(grid, j, elem):
    """Check that each number on a column is used exactly once."""
    col = grid[:, j]
    if elem not in col:
        return True
    return False


def used_in_box(grid, i, j, elem):
    """Check that each number is used exactly once in the box."""
    box_x = i // 3 * 3
    box_y = j // 3 * 3
    box = grid[box_x: box_x + 3, box_y: box_y + 3]
    if elem not in box:
        return True
    return False


def valid(grid, i, j, elem):
    """Check that the number placed at spot i, j is valid."""
    vld = np.zeros(3)
    vld[0] = used_in_row(grid, i, elem)
    vld[1] = used_in_col(grid, j, elem)
    vld[2] = used_in_box(grid, i, j, elem)
    return vld


def find_empty(grid):
    """Find empty spots in the grid."""
    nrows, ncols = grid.shape
    for i in range(nrows):
        for j in range(ncols):
            if grid[i, j] == 0:
                return i, j
    return None


def solve(grid):
    """."""
    find = find_empty(grid)
    if not find:
        return True
    else:
        i, j = find
        for value in range(1, 10):
            if valid(grid, i, j, value).all():
                grid[i, j] = value
                if solve(grid):
                    return True
                grid[i, j] = 0
    return False


# %%
grid = np.array([[0, 2, 0, 6, 0, 0, 0, 0, 8],
                 [0, 0, 0, 0, 5, 0, 9, 0, 1],
                 [0, 0, 0, 0, 0, 1, 0, 7, 0],
                 [0, 0, 0, 0, 4, 0, 0, 6, 7],
                 [0, 0, 8, 5, 0, 6, 3, 0, 0],
                 [1, 3, 0, 0, 8, 0, 0, 0, 0],
                 [0, 5, 0, 2, 0, 0, 0, 0, 0],
                 [3, 0, 2, 0, 6, 0, 0, 0, 0],
                 [4, 0, 0, 0, 0, 5, 0, 9, 0]])

cp = grid.copy()
solve(cp)
print(cp)
