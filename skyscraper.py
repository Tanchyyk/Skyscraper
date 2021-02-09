"""
https://github.com/Tanchyyk/Skyscraper.git
"""


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

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    input_line = input_line[1:][:pivot]

    for i in range(pivot):
        for j in range(i, pivot):
            if input_line[i] > input_line[j]:
                return False
    return True


def right_to_left_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the
    left-most hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> right_to_left_check("412453*", 4)
    True
    >>> right_to_left_check("*524534", 5)
    False
    """
    new_line = str(list(input_line).reverse())
    if left_to_right_check(new_line, pivot):
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
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*', '*543215', '*35214*', '441532*', '*22222*'])
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

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*',\
    '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*',\
    '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*',\
    '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for row in board:
        if left_to_right_check(row, 0) and right_to_left_check(row, 0):
            return True
    return False


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness
    (buildings of unique height) and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one function
    for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*', '*543215',\
    '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*', '*543215',\
    '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*', '*543215',\
    '*35214*', '*41532*', '*2*1***'])
    False
    """
    pass


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.

    >>> check_skyscrapers("check.txt")
    True
    """
    pass


if __name__ == "__main__":
    print(check_skyscrapers("check.txt"))
