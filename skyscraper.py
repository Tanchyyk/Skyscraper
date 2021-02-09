"""
https://github.com/Tanchyyk/Skyscraper.git
"""
import doctest


def read_input(path: str):
    """
    Read game board file from path.
    Return list of str.

    >>> read_input("check.txt")
    ['***21**', '452453*', '423145*', '*543215']
    """
    list_of_rows = []
    with open(path, "r", encoding="utf-8") as file:
        for line in file.readlines():
            list_of_rows.append(line[:-1])
    return list_of_rows


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the
    left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("452453*", 5)
    False
    """
    if input_line[0] == "*":
        return True

    hint = int(input_line[0])
    visible_buildings = 0
    lst_of_nums = []

    for element in input_line:
        if element.isnumeric():
            lst_of_nums.append(int(element))

    for i in range(1, len(lst_of_nums) - 1):
        if lst_of_nums[i] < lst_of_nums[i + 1]:
            visible_buildings += 1
    if visible_buildings >= hint:
        return True
    return False


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?'
    present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*',\
    '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*',\
    '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*',\
    '*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for row in board:
        if "?" in row:
            return False
    return True


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length,
    False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*',\
    '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*',\
    '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*',\
    '*553215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*',\
    '*543215', '*35214*', '441532*', '*22222*'])
    False
    """
    for row in board:
        row = row[1:][:-1].replace("*", "")
        for num in row:
            if row.count(num) > 1:
                return False
    return True


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '452453*', '423145*',\
    '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*',\
    '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    results = []
    for row in board:
        results.append(left_to_right_check(row, 0))
        results.append(left_to_right_check(row[::-1], 0))

    if False not in results:
        return True
    return False


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness
    (buildings of unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function
    for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215',\
    '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215',\
    '*35214*', '*41532*', '*2*1***'])
    False
    """
    new_board = []
    for i in range(len(board)):
        line = []
        for row in board:
            line.append(row[i])
        new_board.append(str(line))

    if check_uniqueness_in_rows(new_board) \
            and check_horizontal_visibility(new_board):
        return True
    return False


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    >>> check_skyscrapers("check.txt")
    False
    """
    board = read_input(input_path)
    if check_not_finished_board(board) and check_uniqueness_in_rows(board) \
            and check_horizontal_visibility(board) and check_columns(board):
        return True
    return False


if __name__ == "__main__":
    print(check_skyscrapers("check.txt"))
    print(doctest.testmod())