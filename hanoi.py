# Towers of Hanoi (UI)

try:
    # import unicurses as curses
    from unicurses import *
except ImportError:
    # import curses
    from curses import *

import curses.ascii

import sys
import pegs
    
stdscr = initscr()
cbreak()
noecho()
stdscr.keypad(True)
stdscr.clear()
curs_set(0)

# getch = stdscr.getch()

# hanoi = pegs.Hanoi()

def hanoi_curses(pieces):
    hanoi = pegs.Hanoi(pieces)
    stdscr.clear()
    title_string = "TOWERS OF HANOI"
    stdscr.addstr(0,0,'====%s====' % ('=' * (len(title_string))))
    stdscr.addstr(1,0,'|   %s   |' % (' ' * len(title_string)))
    stdscr.addstr(2,0,"|   %s   |" % (title_string))
    stdscr.addstr(3,0,'|   %s   |' % (' ' * len(title_string)))
    stdscr.addstr(4,0,'====%s====' % ('=' * (len(title_string))))
    # stdscr.addstr(2,0,'=' * (len(title_string) + 2))
    illegal_move = False
    while not hanoi.win():
        stdscr.addstr(6,0,str(hanoi))
        stdscr.refresh()
        c = stdscr.getch()
        if illegal_move:
            stdscr.addstr(9 + hanoi.pieces,0,"             ")
        if c == ord('q'):
            break
        elif c == ord('n') or c == ord('r'):
            hanoi = pegs.Hanoi(pieces)
            continue
        elif c == KEY_UP or c == ord('w'):
            hanoi.pop()
        elif c == KEY_DOWN or c == ord('s') or c == ord(' '):
            if hanoi.drop():
                illegal_move = True
                stdscr.addstr(9 + hanoi.pieces,0,"Illegal move.")
        elif c == KEY_LEFT or c == ord('a'):
            hanoi.left()
        elif c == KEY_RIGHT or c == ord('d'):
            hanoi.right()
    if hanoi.win():
        stdscr.addstr(6,0,str(hanoi))
        stdscr.refresh()
        stdscr.addstr(9 + hanoi.pieces,0,"You win!")
        stdscr.addstr(10 + hanoi.pieces,0,"Again? Y/N")
        c = stdscr.getch()
        while c not in [ord('q'), ord('n'), ord('y'), ord('N'), ord('Y')]:
            c = stdscr.getch()
        if c in [ord('y'), ord('Y')]:
            return True
    return False

hanoi_solutions = {1: [pegs.Hanoi.pop, pegs.Hanoi.right, pegs.Hanoi.right, pegs.Hanoi.drop]}

# 2: []

def hanoi_solve_memoized(hanoi):
    if hanoi.pieces in hanoi_solutions:
        return hanoi_solutions[hanoi.pieces]
    # pieces = 1
    # while pieces < hanoi.pieces:
    # hanoi_solutions[hanoi.pieces]

def hanoi_solve_recursive(hanoi):
    return

def invader_curses(invaders):
    return

try:
    pieces = int(sys.argv[1])
except IndexError:
    pieces = 3

try:
    while hanoi_curses(pieces):
        pieces += 1
    # # 
    # while not hanoi.win():
    #     stdscr.addstr(0,0,str(hanoi))
    #     stdscr.refresh()
    #     c = stdscr.getch()
    #     if c == ord('q'):
    #         break
    #     elif c == ord('n'):
    #         hanoi = pegs.Hanoi()
    #         continue
    #     elif c == KEY_UP or c == ord('w'):
    #         hanoi.pop()
    #     elif c == KEY_DOWN or c == ord('s'):
    #         hanoi.drop()
    #     elif c == KEY_LEFT or c == ord('a'):
    #         hanoi.left()
    #     elif c == KEY_RIGHT or c == ord('d'):
    #         hanoi.right()
    # if hanoi.win():
    #     stdscr.addstr(0,0,str(hanoi))
    #     stdscr.refresh()
    #     stdscr.addstr(6,0,"You win!")
    # stdscr.getch()
except (KeyboardInterrupt, ImportError, NameError):
    pass
finally:
    nocbreak()
    stdscr.keypad(False)
    echo()
    endwin()
