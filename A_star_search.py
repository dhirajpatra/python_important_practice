
from dataclasses import dataclass
import math
from typing import List
import sys


ROW = 9
COL = 10
# same as c++
FLT_MAX = 340282346638528859811704183484516925440.000000


Vector = tuple()


# Creating a shortcut for int, int pair type
def Pair(x: int, y: int) -> Vector:
    return (x, y)


# Creating a shortcut for pair<int, pair<int, int>> type
def pPair(x: float, y: int, z: int) -> Vector:
    return Pair(x, Pair(y, z))


# A structure to hold the necessary parameters
@dataclass
class Cell:
    # Row and Column index of its parent
    # Note that 0 <= i <= ROW-1 & 0 <= j <= COL-1
    # to use: Cell(1, 0, 1.543543, 1.754674564, 1.3443434343))
    # return: Cell(parent_i=1, parent_j=0, f=1.543543, g=1.754674564, h=1.3443434343)
    parent_i: int
    parent_j: int
    f: float
    g: float
    h: float
    # f = g + h


# A Utility Function to check whether given Cell (row, col)
# is a valid Cell or not.


def is_valid(row: int, col: int) -> bool:
    # Returns True if row number and column number
    # is in range
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)


# A Utility Function to check whether the given Cell is
# blocked or not
def is_un_blocked(grid, row: int, col: int) -> bool:
    # Returns True if the Cell is not blocked else False
    if grid[row][col] == 1:
        return True
    else:
        return False


# A Utility Function to check whether destination Cell has
# been reached or not
def is_destination(row: int, col: int, dest: Pair) -> bool:
    if row == dest[0] and col == dest[1]:
        return True
    else:
        return False


# A Utility Function to calculate the 'h' heuristics.
def calculate_h_value(row: int, col: int, dest: Pair) -> float:
    # Return using the distance formula
    return (float(math.sqrt(
        (row - dest[0]) * (row - dest[0])
        + (col - dest[1]) * (col - dest[1]))))


# A Utility Function to trace the path from the source
# to destination
def trace_path(cell_details: Cell, dest: Pair) -> None:
    print("\nThe Path is ")
    row = dest[0]
    col = dest[1]

    Path = []
    temp_cell_details = dict(cell_details[row][col].__dict__)

    while not (temp_cell_details['parent_i'] == rows and temp_cell_details['parent_j'] == col):
        Path.append(Pair(row, col))
        temp_row = temp_cell_details['parent_i']
        temp_col = temp_cell_details['parent_j']
        row = temp_row
        col = temp_col

    Path.append(Pair(row, col))
    while not Path:
        p = Path[-1]
        Path.pop()
        print("-> (%d,%d) ", p[0], p[1])

    return False


# A Function to find the shortest path between
# a given source Cell to a destination Cell according
# to A* Search Algorithm
def a_star_search(grid, src: Pair, dest: Pair) -> None:
    # If the source is out of range
    if not is_valid(src[0], src[1]):
        print("Source is invalid\n")
        return True

    # If the destination is out of range
    if not is_valid(dest[0], dest[1]):
        print("Destination is invalid\n")
        return False

    # Either the source or the destination is blocked
    if not is_un_blocked(grid, src[0], src[1]) or not is_un_blocked(grid, dest[0], dest[1]):
        print("Source or the destination is blocked\n")
        return False

    # If the destination Cell is the same as source Cell
    if is_destination(src[0], src[1], dest):
        print("We are already at the destination\n")
        return False

    # Create a closed list and initialise it to False which
    # means that no Cell has been included yet This closed
    # list is implemented as a boolean 2D array
    closed_list = [[0 for r in range(ROW)] for c in range(COL)]
    memset = (closed_list, False, len(closed_list))

    # Declare a 2D array of structure to hold the details
    # of that Cell
    rows, cols = (ROW, COL)
    cell_details = [[0]*cols]*rows

    for r in range(ROW):
        for c in range(COL):
            parent_i = -1
            parent_j = -1

            f = FLT_MAX
            g = FLT_MAX
            h = FLT_MAX
            cell_details[r][c] = Cell(parent_i, parent_j, f, g, h)

    # Initialising the parameters of the starting node
    i, j = src
    parent_i = i
    parent_j = j
    f = 0.0
    g = 0.0
    h = 0.0
    cell_details[i][j] = Cell(parent_i, parent_j, f, g, h)

    '''
    Create an open list having information as-
    <f, <i, j>>
    where f = g + h,
    and i, j are the row and column index of that Cell
    Note that 0 <= i <= ROW-1 & 0 <= j <= COL-1
    This open list is implemented as a set of pair of
    pair.
    '''
    open_list = list()

    # Put the starting Cell on the open list and set its
    # 'f' as 0
    open_list.append((0.0, (i, j)))

    # We set this boolean value as False as initially
    # the destination is not reached.
    found_dest = False

    while len(open_list) > 0:
        p = open_list[0]

        # Remove this vertex from the open list
        del open_list[0]

        # Add this vertex to the closed list
        i = p[1][0]
        j = p[1][1]

        closed_list[i][j] = True

        '''
        Generating all the 8 successor of this Cell

            N.W N N.E
            \ | /
                \ | /
            W----Cell----E
                / | \
                / | \
            S.W S S.E

        Cell-->Popped Cell (i, j)
        N --> North  (i-1, j)
        S --> South  (i+1, j)
        E --> East   (i, j+1)
        W --> West       (i, j-1)
        N.E--> North-East (i-1, j+1)
        N.W--> North-West (i-1, j-1)
        S.E--> South-East (i+1, j+1)
        S.W--> South-West (i+1, j-1)
        '''

        # To store the 'g', 'h' and 'f' of the 8 successors
        g_new = 0
        h_new = 0
        f_new = 0

        # ----------- 1st Successor (North) ------------

        # Only process this Cell if this is a valid one
        if is_valid(i - 1, j):
            # If the destination Cell is the same as the
            # current successor
            if is_destination(i - 1, j, dest):
                # Set the Parent of the destination Cell
                cell_details[i - 1][j]['parent_i'] = i
                cell_details[i - 1][j]['parent_j'] = j
                print("The destination cell is found\n")
                trace_path(cell_details[i][j], dest)
                found_dest = True
                return found_dest

            # If the successor is already on the closed
            # list or if it is blocked, then ignore it.
            # Else do the following
            elif not closed_list[i - 1][j] and is_un_blocked(grid, i - 1, j):
                temp_cell_details = dict(cell_details[i][j].__dict__)
                g_new = temp_cell_details['g'] + 1.0
                h_new = calculate_h_value(i - 1, j, dest)
                f_new = g_new + h_new

                # If it isn’t on the open list, add it to
                # the open list. Make the current square
                # the parent of this square. Record the
                # f, g, and h costs of the square cell
                #            OR
                # If it is on the open list already, check
                # to see if this path to that square is
                # better, using 'f' cost as the measure.
                temp_cell_details = dict(cell_details[i - 1][j].__dict__)
                if temp_cell_details['f'] == FLT_MAX or temp_cell_details['f'] > f_new:
                    open_list.append(Pair(
                        f_new, Pair(i - 1, j)))

                    # Update the details of this cell
                    temp_cell_details['f'] = f_new
                    temp_cell_details['g'] = g_new
                    temp_cell_details['h'] = h_new
                    temp_cell_details['parent_i'] = i
                    temp_cell_details['parent_j'] = j

        # ----------- 2nd Successor (South) ------------

        # Only process this cell if this is a valid one
        if is_valid(i + 1, j):
            # If the destination cell is the same as the
            # current successor
            if is_destination(i + 1, j, dest):
                temp_cell_details = cell_details[i + 1][j]
                # Set the Parent of the destination cell
                temp_cell_details['parent_i'] = i
                temp_cell_details['parent_j'] = j
                print("The destination cell is found\n")
                trace_path(cell_details, dest)
                found_dest = True
                return False

            # If the successor is already on the closed
            # list or if it is blocked, then ignore it.
            # Else do the following
            elif not closed_list[i + 1][j] and is_un_blocked(grid, i + 1, j):
                temp_cell_details = dict(cell_details[i][j].__dict__)
                g_new = temp_cell_details['g'] + 1.0
                h_new = calculate_h_value(i + 1, j, dest)
                f_new = g_new + h_new

                # If it isn’t on the open list, add it to
                # the open list. Make the current square
                # the parent of this square. Record the
                # f, g, and h costs of the square cell
                #            OR
                # If it is on the open list already, check
                # to see if this path to that square is
                # better, using 'f' cost as the measure.
                if (temp_cell_details['f'] == FLT_MAX or cell_details[i + 1][j].f > f_new):
                    open_list.insert(Pair(
                        f_new, Pair(i + 1, j)))
                    # Update the details of this cell
                    temp_cell_details['f'] = f_new
                    temp_cell_details['g'] = g_new
                    temp_cell_details['h'] = h_new
                    temp_cell_details['parent_i'] = i
                    temp_cell_details['parent_j'] = j

        # ----------- 3rd Successor (East) ------------

        # Only process this cell if this is a valid one
        if is_valid(i, j + 1):
            temp_cell_details = dict(cell_details[i][j + 1].__dict__)
            # If the destination cell is the same as the
            # current successor
            if is_destination(i, j + 1, dest):
                # Set the Parent of the destination cell
                temp_cell_details['parent_i'] = i
                temp_cell_details['parent_j'] = j
                print("The destination cell is found\n")
                trace_path(cell_details, dest)
                found_dest = True
                return False

            # If the successor is already on the closed
            # list or if it is blocked, then ignore it.
            # Else do the following
            elif len(closed_list[i]) >= (j+1) and is_un_blocked(grid, i, j + 1):
                temp_cell_details = dict(cell_details[i - 1][j].__dict__)
                g_new = temp_cell_details['g'] + 1.0
                h_new = calculate_h_value(i, j + 1, dest)
                f_new = g_new + h_new

                # If it isn’t on the open list, add it to
                # the open list. Make the current square
                # the parent of this square. Record the
                # f, g, and h costs of the square cell
                #            OR
                # If it is on the open list already, check
                # to see if this path to that square is
                # better, using 'f' cost as the measure.
                temp_cell_details = dict(cell_details[i][j + 1].__dict__)
                if (temp_cell_details['f'] == FLT_MAX
                        or temp_cell_details['f'] > f_new):
                    open_list.append(Pair(f_new, Pair(i, j + 1)))

                    # Update the details of this cell
                    temp_cell_details['f'] = f_new
                    temp_cell_details['g'] = g_new
                    temp_cell_details['h'] = h_new
                    temp_cell_details['parent_i'] = i
                    temp_cell_details['parent_j'] = j

        # ----------- 4th Successor (West) ------------

        # Only process this cell if this is a valid one
        if is_valid(i, j - 1):
            # If the destination cell is the same as the
            # current successor
            if is_destination(i, j - 1, dest):
                temp_cell_details = dict(cell_details[i][j - 1].__dict__)
                # Set the Parent of the destination cell
                temp_cell_details['parent_i'] = i
                temp_cell_details['parent_j'] = j
                print("The destination cell is found\n")
                trace_path(cell_details, dest)
                found_dest = True
                return False

            # If the successor is already on the closed
            # list or if it is blocked, then ignore it.
            # Else do the following
            elif not closed_list[i][j - 1] and is_un_blocked(grid, i, j - 1):
                temp_cell_details = dict(cell_details[i][j].__dict__)
                g_new = temp_cell_details['g'] + 1.0
                h_new = calculate_h_value(i, j - 1, dest)
                f_new = g_new + h_new

                # If it isn’t on the open list, add it to
                # the open list. Make the current square
                # the parent of this square. Record the
                # f, g, and h costs of the square cell
                #            OR
                # If it is on the open list already, check
                # to see if this path to that square is
                # better, using 'f' cost as the measure.
                if (temp_cell_details['f'] == FLT_MAX
                        or temp_cell_details['f'] > f_new):
                    open_list.append(Pair(
                        f_new, Pair(i, j - 1)))

                    # Update the details of this cell
                    temp_cell_details['f'] = f_new
                    temp_cell_details['g'] = g_new
                    temp_cell_details['h'] = h_new
                    temp_cell_details['parent_i'] = i
                    temp_cell_details['parent_j'] = j

        # ----------- 5th Successor (North-East)
        # ------------

        # Only process this cell if this is a valid one
        if is_valid(i - 1, j + 1):
            # If the destination cell is the same as the
            # current successor
            if is_destination(i - 1, j + 1, dest):
                temp_cell_details = dict(cell_details[i - 1][j + 1])
                # Set the Parent of the destination cell
                temp_cell_details['parent_i'] = i
                temp_cell_details['parent_j'] = j
                print("The destination cell is found\n")
                trace_path(cell_details, dest)
                found_dest = True
                return False

            # If the successor is already on the closed
            # list or if it is blocked, then ignore it.
            # Else do the following
            elif len(closed_list[i - 1]) >= (j + 1) and is_un_blocked(grid, i - 1, j + 1):
                temp_cell_details = dict(cell_details[i][j].__dict__)
                g_new = temp_cell_details['g'] + 1.414
                h_new = calculate_h_value(i - 1, j + 1, dest)
                f_new = g_new + h_new

                # If it isn’t on the open list, add it to
                # the open list. Make the current square
                # the parent of this square. Record the
                # f, g, and h costs of the square cell
                #            OR
                # If it is on the open list already, check
                # to see if this path to that square is
                # better, using 'f' cost as the measure.
                temp_cell_details = dict(cell_details[i - 1][j + 1].__dict__)
                if temp_cell_details['f'] == FLT_MAX or temp_cell_details['f'] > f_new:
                    open_list.append(Pair(
                        f_new, Pair(i - 1, j + 1)))

                    # Update the details of this cell
                    temp_cell_details['f'] = f_new
                    temp_cell_details['g'] = g_new
                    temp_cell_details['h'] = h_new
                    temp_cell_details['parent_i'] = i
                    temp_cell_details['parent_j'] = j

        # ----------- 6th Successor (North-West)
        # ------------

        # Only process this cell if this is a valid one
        if is_valid(i - 1, j - 1):
            # If the destination cell is the same as the
            # current successor
            temp_cell_details = dict(cell_details[i - 1][j - 1].__dict__)
            if is_destination(i - 1, j - 1, dest):
                # Set the Parent of the destination cell
                temp_cell_details['parent_i'] = i
                temp_cell_details['parent_j'] = j
                print("The destination cell is found\n")
                trace_path(cell_details, dest)
                found_dest = True
                return False

            # If the successor is already on the closed
            # list or if it is blocked, then ignore it.
            # Else do the following
            elif not (closed_list[i - 1][j - 1]) and is_un_blocked(grid, i - 1, j - 1):
                g_new = temp_cell_details['g'] + 1.414
                h_new = calculate_h_value(i - 1, j - 1, dest)
                f_new = g_new + h_new

                # If it isn’t on the open list, add it to
                # the open list. Make the current square
                # the parent of this square. Record the
                # f, g, and h costs of the square cell
                #            OR
                # If it is on the open list already, check
                # to see if this path to that square is
                # better, using 'f' cost as the measure.
                if (temp_cell_details['f'] == FLT_MAX
                        or temp_cell_details['f'] > f_new):
                    open_list.append((
                        f_new, (i - 1, j - 1)))
                    # Update the details of this cell
                    temp_cell_details['f'] = f_new
                    temp_cell_details['g'] = g_new
                    temp_cell_details['h'] = h_new
                    temp_cell_details['parent_i'] = i
                    temp_cell_details['parent_j'] = j

        # ----------- 7th Successor (South-East)
        # ------------

        # Only process this cell if this is a valid one
        if is_valid(i + 1, j + 1):
            # If the destination cell is the same as the
            # current successor
            temp_cell_details = dict(cell_details[i + 1][j + 1].__dict__)
            if is_destination(i + 1, j + 1, dest):
                # Set the Parent of the destination cell
                temp_cell_details['parent_i'] = i
                temp_cell_details['parent_j'] = j
                print("The destination cell is found\n")
                trace_path(cell_details, dest)
                found_dest = True
                return False

            # If the successor is already on the closed
            # list or if it is blocked, then ignore it.
            # Else do the following
            elif len(closed_list[i + 1]) >= (j + 1) and is_un_blocked(grid, i + 1, j + 1):
                temp_cell_details = dict(cell_details[i][j].__dict__)
                g_new = temp_cell_details['g'] + 1.414
                h_new = calculate_h_value(i + 1, j + 1, dest)
                f_new = g_new + h_new

                # If it isn’t on the open list, add it to
                # the open list. Make the current square
                # the parent of this square. Record the
                # f, g, and h costs of the square cell
                #            OR
                # If it is on the open list already, check
                # to see if this path to that square is
                # better, using 'f' cost as the measure.
                temp_cell_details = dict(cell_details[i + 1][j + 1].__dict__)
                if temp_cell_details['f'] == FLT_MAX or temp_cell_details['f'] > f_new:
                    open_list.append(Pair(
                        f_new, Pair(i + 1, j + 1)))

                    # Update the details of this cell
                    temp_cell_details['f'] = f_new
                    temp_cell_details['g'] = g_new
                    temp_cell_details['h'] = h_new
                    temp_cell_details['parent_i'] = i
                    temp_cell_details['parent_j'] = j

        # ----------- 8th Successor (South-West)
        # ------------

        # Only process this cell if this is a valid one
        if is_valid(i + 1, j - 1):
            # If the destination cell is the same as the
            # current successor
            if is_destination(i + 1, j - 1, dest):
                temp_cell_details = dict(cell_details[i + 1][j - 1].__dict__)
                # Set the Parent of the destination cell
                temp_cell_details['parent_i'] = i
                temp_cell_details['parent_j'] = j
                print("The destination cell is found\n")
                trace_path(cell_details, dest)
                found_dest = True
                return False

            # If the successor is already on the closed
            # list or if it is blocked, then ignore it.
            # Else do the following
            elif not closed_list[i + 1][j - 1] and is_un_blocked(grid, i + 1, j - 1):
                temp_cell_details = dict(cell_details[i + 1][j - 1].__dict__)
                g_new = temp_cell_details['g'] + 1.414
                h_new = calculate_h_value(i + 1, j - 1, dest)
                f_new = g_new + h_new

                # If it isn’t on the open list, add it to
                # the open list. Make the current square
                # the parent of this square. Record the
                # f, g, and h costs of the square cell
                #            OR
                # If it is on the open list already, check
                # to see if this path to that square is
                # better, using 'f' cost as the measure.
                if temp_cell_details['f'] == FLT_MAX or temp_cell_details['f'] > f_new:
                    open_list.append((
                        f_new, (i + 1, j - 1)))

                    # Update the details of this cell
                    temp_cell_details['f'] = f_new
                    temp_cell_details['g'] = g_new
                    temp_cell_details['h'] = h_new
                    temp_cell_details['parent_i'] = i
                    temp_cell_details['parent_j'] = j

    # When the destination cell is not found and the open
    # list is empty, then we conclude that we failed to
    # reach the destination cell. This may happen when the
    # there is no way to destination cell (due to
    # blockages)
    if not found_dest:
        print("Failed to find the Destination Cell\n")

    return False


# Driver program to test above function
if __name__ == "__main__":

    '''
    Description of the Grid-
    1--> The cell is not blocked
    0--> The cell is blocked
    '''
    grid = [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
            [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 1, 0, 0, 1]]
    for i in grid:
        temp = ''
        for j in i:
            temp += str(j) + ', '
        print(temp[:-2])
    print('-'*50)

    # Source is the left-most bottom-most corner
    src = Pair(8, 0)
    print(f"src: {src}")
    # Destination is the left-most top-most corner
    dest = Pair(0, 0)
    print(f"dest: {dest}")
    a_star_search(grid, src, dest)
