import curses
from curses import wrapper


def main(stdscr):
    # int is an id representing the pair / text color / background color
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_WHITE)
    stdscr.addstr("hello world", curses.color_pair(1))


wrapper(main)
