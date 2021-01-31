
""" 
Given an N by M grid filled with integers find the “cluster” whose value is closest to the average value of all clusters in the grid.

 A cluster is defined as a 3 by 3 grouping within the grid and is identified by the
 index of upper left corner within the cluster. Its value is the sum of integers
 contained within the cluster. Clusters can also overlap.
 
Example 1: inputs: grid, 
{1, 2, 3},
{4, 5, 6},
{7, 8, 9}


Example 2:
{1, 2, 3, 1},
{4, 5, 6, 7},
{7, 8, 9, 2}


Example 3:
{1, 2, 3, 4, 5, 6},
{6, 8, 0, 7, 0, 6},
{6, 8, 9, 1, 7, 6},
{1, 3, 0, 4, 3, 5},
{0, 2, 9, 4, 3, 3}

"""


def find_cluster_average(grid):
    if not grid:
        return

    row_length = len(grid)
    col_length = len(grid[0])
    cluster_count = 0
    total = 0
    for row in range(row_length - 2):
        for col in range(col_length - 2):
            total += get_sub_grid_total(grid, row, col)
            cluster_count += 1

    avg = total/cluster_count


def get_sub_grid_total(grid, row, col):
    """
     3x3 grid only
    """
    total = 0

    for i in range(row, row + 3):
        for j in range(col, col + 3):
            total += grid[i][j]

    return total
