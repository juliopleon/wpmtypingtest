import curses
from curses import wrapper


def start_screen(stdscr):
    stdscr.clear()
    # text position: row position than column
    stdscr.addstr(0, 0, "Welcome to the WPM Typing Test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()


def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)

    for i, char in enumerate(current):
        # start on index 0 so on, i is the char inserted
        stdscr.addstr(0, i, char, curses.color_pair(1))


def wpm_test(stdscr):
    target_text = "Hello world this is some text for the testing for the app!"
    current_text = []

    while True:
        stdscr.clear()
        display_text(stdscr, target_text, current_text)
        stdscr.refresh()

        key = stdscr.getkey()
        # ordinal value 27 == escape
        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        else:
            current_text.append(key)


def main(stdscr):
    # int is an id representing the pair / text color / background color
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)


wrapper(main)
