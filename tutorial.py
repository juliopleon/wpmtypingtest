import curses
from curses import wrapper


def start_screen(stdscr):
    stdscr.clear()
    # text position: row position than column
    stdscr.addstr(0, 0, "Welcome to the WPM Typing Test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()


def wpm_test(stdscr):
    target_text = "Hello world this is some text for the testing for the app!"
    current_text = []

    stdscr.clear()
    stdscr.addstr(target_text)
    stdscr.refresh()
    stdscr.getkey()


def main(stdscr):
    # int is an id representing the pair / text color / background color
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)


wrapper(main)
