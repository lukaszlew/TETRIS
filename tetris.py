from dataclasses import dataclass
import random
from copy import deepcopy

# BOARD

# - lista list z integerami
# - wymiary zawsze 10x20
# - 0 oznacza puste pole
# - 1 oznacza shape'a
# - 2 oznacza granicę boarda
# - 5 górnych rows służy jako miejsce do wstawiania shape'ów
# - gra się kończy kiedy 1 pojawi się na row <= 5

board = [[0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,0,0,0,0,0,0,0,0,2],
         [2,2,2,2,2,2,2,2,2,2],]

# SHAPES

# - wymiar listy list z kształtem to zawsze 5x5
# - 0 to puste pole a 1 kawałek klocka
# - kształty są zapisane na liście shapes
# - każdy kształt jest listą, w której są zapisane
#   listy list z integerami. Każda lista list obrazuje
#   unikalne ułożenie klocka
# - elementy listy to wszystkie możliwe rotacje shape'a
# - element 0 jest zawsze startowym ułożeniem shape'a
# - przy rotacji shape zmienia ułożenie zgodnie z kolejnością na liście
# - kiedy ma się zmienić ostatnia rotacja --> przeskok na początek listy i shape
# - jest w ustawieniu początkowym

S = [[[0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,1,1,0],
      [0,1,1,0,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,0,1,0,0],
      [0,0,1,1,0],
      [0,0,0,1,0],
      [0,0,0,0,0]]]

Z = [[[0,0,0,0,0],
      [0,0,0,0,0],
      [0,1,1,0,0],
      [0,0,1,1,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,0,1,0,0],
      [0,1,1,0,0],
      [0,1,0,0,0],
      [0,0,0,0,0]]]
 
I = [[[0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [1,1,1,1,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0]]]
 
O = [[[0,0,0,0,0],
      [0,0,0,0,0],
      [0,1,1,0,0],
      [0,1,1,0,0],
      [0,0,0,0,0]]]
     
J = [[[0,0,0,0,0],
      [0,1,0,0,0],
      [0,1,1,1,0],
      [0,0,0,0,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,0,1,1,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,0,0,0,0],
      [0,1,1,1,0],
      [0,0,0,1,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,1,1,0,0],
      [0,0,0,0,0]]]
 
L = [[[0,0,0,0,0],
      [0,0,0,1,0],
      [0,1,1,1,0],
      [0,0,0,0,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,1,1,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,0,0,0,0],
      [0,1,1,1,0],
      [0,1,0,0,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,1,1,0,0],
      [0,0,1,0,0],
      [0,0,1,0,0],
      [0,0,0,0,0]]]
 
T = [[[0,0,0,0,0],
      [0,0,1,0,0],
      [0,1,1,1,0],
      [0,0,0,0,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,0,1,0,0],
      [0,0,1,1,0],
      [0,0,1,0,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,0,0,0,0],
      [0,1,1,1,0],
      [0,0,1,0,0],
      [0,0,0,0,0]],
     [[0,0,0,0,0],
      [0,0,1,0,0],
      [0,1,1,0,0],
      [0,0,1,0,0],
      [0,0,0,0,0]]]

shapes = [S, Z, I, O, J, L, T]

# CLASSES

@dataclass
class pos:
    row: int
    col: int

@dataclass
class val:
    pos: pos
    num: int

# SHAPE STARTING POSITION

# starting_pos to lista list z pos
# każda pos oznacza pozycję startową na boardzie dla nowo powstałego
# shape'a

starting_pos = [[pos(0,3),pos(0,4),pos(0,5),pos(0,6),pos(0,7)],
                [pos(1,3),pos(1,4),pos(1,5),pos(1,6),pos(1,7)],
                [pos(2,3),pos(2,4),pos(2,5),pos(2,6),pos(2,7)],
                [pos(3,3),pos(3,4),pos(3,5),pos(3,6),pos(3,7)],
                [pos(4,3),pos(4,4),pos(4,5),pos(4,6),pos(4,7)]]

# FUNCTIONS

def set_shape_pos(shape, pos_set):
    for i in range(5):
        for j in range(5):
            shape[i][j] = val(pos_set[i][j], shape[i][j])

def print_board(board, shape):
    board_to_print = deepcopy(board)

    # dodawanie obecnego shape'a na board_to_print
    for row in shape:
        for val in row:
            if val.num == 1:
                board_to_print[val.pos.row][val.pos.col] = 1

    # printing board_to_print
    for row in board_to_print:
        print(row)

    return

def pick_new_random_shape(shapes):
    curr_shape_ind = random.randint(0, 6)
    shape, shape_rot_num = shapes[curr_shape_ind][0], 0
  
    return shape, shape_rot_num, curr_shape_ind

def rotate_shape(shapes, shape, shape_rot_num, curr_shape_ind):
    old_shape = deepcopy(shape)
    old_shape_rot_num = shape_rot_num
    curr_pos = save_curr_shape_pos(shape)
    new_shape, new_shape_rot_num = change_shape_rotation(shapes, shape_rot_num, curr_shape_ind)
    set_shape_pos(new_shape, curr_pos)

    return old_shape, new_shape, old_shape_rot_num, new_shape_rot_num

def save_curr_shape_pos(shape):
    curr_pos = []
  
    for row in shape:
        new_row = []
        for val in row:
            new_row.append(val.pos)
        curr_pos.append(new_row)

    return curr_pos

def change_shape_rotation(shapes, shape_rot_num, curr_shape_ind):
    if shape_rot_num < len(shapes[curr_shape_ind]) - 1:
        shape_rot_num += 1
    else:
        shape_rot_num = 0

    print(curr_shape_ind)
    print(shape_rot_num)
    shape = shapes[curr_shape_ind][shape_rot_num]

    return shape, shape_rot_num

def check_if_collide(board, shape):
    for row in shape:
        for val in row:
            if val.num == 1 and board[val.pos.row][val.pos.col] == 1 or board[val.pos.row][val.pos.col] == 2:
                return True
    return False

def move_shape(shape, input_move = 's'):
    old_shape = deepcopy(shape)
    delta_pos = {
    's' : pos(1, 0), 
    'a' : pos(0, -1),
    'd' : pos(0, 1),
    '' : pos(0, 0),
    }

    assert input_move in ['a', 's', 'd', '']
    for row in shape:
        for val in row:
            val.pos = add_pos(val.pos, delta_pos[input_move])

    return old_shape, shape

def add_pos(p, delta):
    return pos(p.row + delta.row, p.col + delta.col)

def add_shape_to_board(board, shape):
    for row in shape:
        for val in row:
            if val.num == 1:
                board[val.pos.row][val.pos.col] = 1
    return

def remove_full_rows(board):
    len_row_no_border = len(board[0][1:-1])
  
    for i in range(len(board[5:])):
        count = 0
        for j in range(1, len(board[0][:-1])):
            if board[i][j] == 1:
                count += 1
        if count == len_row_no_border:
            remove_row_and_adapt_board(board, i)
            remove_full_rows(board)
  
    return

def remove_row_and_adapt_board(board, i):
    # czyszczenie pełnego rzędu i
    for j in range(1, len(board[0][:-1])):
        board[i][j] = 0

    # opuszczanie wszystkich 1 powyżej rzędu 'i' o 1 w dół
    for x in range(len(board[i]),5,-1):
        for y in range(1, len(board[0][:-1])):
            if board[x][y] == 1:
                board[x][y], board[x+1][y] = 0, 1

def check_if_game_over(board):
    for i in range(5):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                return False
    return True

def tetris(board, shapes):
    is_running = True
    is_moving = False
    shape = []
    print_board(board, shape)

    while is_running:
        if is_moving is False:
            shape, shape_rot_num, curr_shape_ind = pick_new_random_shape(shapes)
            set_shape_pos(shape, starting_pos)
            print_board(board, shape)
        else:
            input_rotate = input('type y if rotate, n if not:')
            assert input_rotate in ['y', 'n']
            if input_rotate == 'y':
                old_shape, shape,  old_shape_rot_num, shape_rot_num = rotate_shape(shapes, shape, shape_rot_num, curr_shape_ind)
                collision = check_if_collide(board, shape)
                if collision:
                    shape, shape_rot_num = old_shape, old_shape_rot_num
            print_board(board, shape)
            input_move = input('type a if move left, d if right, '' if not')
            assert input_move in ['a', 'd', '']
            old_shape, shape = move_shape(shape, input_move)
            collision = check_if_collide(board, shape)
            if collision:
                shape = old_shape
            print_board(board, shape)
        is_moving = True
        old_shape, shape = move_shape(shape)
        collision = check_if_collide(board, shape)
        if collision:
            shape = old_shape
            is_moving = False
            add_shape_to_board(board, shape)
            remove_full_rows(board)
        print_board(board, shape)
        is_running = check_if_game_over(board)

    return 'Game over'

# TESTY
# shape = S[0]
# set_shape_pos(shape, starting_pos)
# print_board(board, shape)
# old_shape, shape = move_shape(shape)
# print('')
# print_board(board, shape)
# old_shape, shape = move_shape(shape, 'a')
# print('')
# print_board(board, shape)
# old_shape, shape = move_shape(shape, 'd')
# print('')
# print_board(board, shape)
# shape_rot_num = 0
# old_shape, shape, old_shape_rot_num, shape_rot_num = rotate_shape(shapes, shape, shape_rot_num, 0)
# print('')
# print_board(board, shape)

tetris(board, shapes)