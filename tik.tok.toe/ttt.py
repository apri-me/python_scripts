from prettytable import PrettyTable as PT
from random import randrange
from time import sleep


def get_player_side():
    my_side = input("Choose your side(X or O): ")
    while not ( my_side.capitalize() == 'X' or my_side.capitalize() == 'O'):
        print("Wrong choice")
        my_side = input("Choose your side(X or O): ")
    my_side = my_side.capitalize()
    return my_side

def get_play_ground():
    play_ground = []
    for i in range(3):
        play_ground.append([])
        for j in range(3):
            play_ground[i].append(" ")
    return play_ground


def is_emp(i, j, play_ground):
    return play_ground[i][j] == " "


def emp_number(play_ground):
    ct = 0
    for i in range(3):
        for j in range(3):
            if is_emp(i, j, play_ground):
                ct += 1
    return ct

def com_move(play_ground, com_side):
    r = randrange(emp_number(play_ground))
    ct = 0
    for i in range(3):
        for j in range(3):
            if is_emp(i, j, play_ground):
                if ct == r:
                    play_ground[i][j] = com_side
                    return
                ct += 1

def is_good_choice(i, j, play_ground):
    if 0 <= i <= 3 and 0 <= j <= 3 and is_emp(i, j, play_ground):
        return True
    return False

def get_player_ans():
    return ( int( input('row: ')) - 1, int( input('col: ')) - 1)

def player_move(play_ground, player_side):
    print("Enter the row and col of your choice:")
    ans = get_player_ans()
    while not is_good_choice(*ans, play_ground):
        print("Enter a correct and empty element")
        ans = get_player_ans()
    play_ground[ans[0]][ans[1]] = player_side


def show_table(play_ground):
    pt = PT( [" ", 1, 2, 3] )
    for i in range(3):
        pt.add_row([i+1] + play_ground[i])
    print(pt)

def act_next_move(play_ground, player_side, com_side):
    if emp_number(play_ground) % 2 == 0:
        com_move(play_ground, com_side)
    else:
        player_move(play_ground, player_side)

def got_triple(l, play_ground):
    for i in range(3):
        for j in range(3):
            if play_ground[i][j] != l:
                break
            elif j == 2:
                return True
    for j in range(3):
        for i in range(3):
            if play_ground[i][j] != l:
                break
            elif i == 2:
                return True
    for i in range(3):
        if play_ground[i][i] != l:
            break
        elif i == 2:
            return True
    for i in range(3):
        if play_ground[i][2 - i] != l:
            break
        elif i == 2:
            return True
    return False

def check_who_wins(play_ground):
    for l in ('X', 'O'):
        if got_triple(l, play_ground):
            return l

player_side = get_player_side()
com_side = 'X' if player_side == 'O' else 'O'
play_ground= get_play_ground()
show_table(play_ground)
while (emp_number(play_ground) != 0):
    act_next_move(play_ground, player_side, com_side)
    show_table(play_ground)
    sleep(3)
    wining_state = check_who_wins(play_ground)
    if wining_state:
        break

print(f'{wining_state} won the game!')