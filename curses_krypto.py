#!/usr/bin/python3
import curses
import time


def choose_crypt(stdscr, current_index, y_axis):
    stdscr.attron(curses.color_pair(3))
    stdscr.addstr(y_axis, 0, current_index)
    stdscr.refresh()
    stdscr.attroff(curses.color_pair(3))


def slow(text, y_axis, stdscr):
    x_axis = 0
    for char in text:
        stdscr.addstr(y_axis, x_axis, char)
        stdscr.refresh()
        x_axis += 1
        time.sleep(0.09)


def main(stdscr):
    curses.echo()
    y_axis = 0
    machine_color = 1
    user_input_color = 2
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    # for normal teks som man ikke skrive
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    # for noget man selv skriver
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_GREEN)
    # for selected
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
    # for det man skal bruge
    stdscr.attron(curses.color_pair(machine_color))
    # her starter den med at skrive
    slow('Giv din key', y_axis, stdscr)
    stdscr.attron(curses.color_pair(user_input_color))
    user_key = stdscr.getstr(1, 0)
    stdscr.clear()
    while True:
        stdscr.attron(curses.color_pair(machine_color))
        slow('1: Incrypt', y_axis, stdscr)
        y_axis += 1
        slow('2: Decrypt', y_axis, stdscr)
        y_axis += 1
        menu = True
        while menu:
            key = stdscr.getch()
            if key == curses.KEY_UP:
                current_index = "1: Incrypt"
                stdscr.attron(curses.color_pair(machine_color))
                stdscr.addstr(y_axis - 1, 0, "2: Decrypt")
                stdscr.refresh()
                choose_crypt(stdscr, current_index, y_axis - 2)
            if key == curses.KEY_DOWN:
                current_index = "2: Decrypt"
                stdscr.attron(curses.color_pair(machine_color))
                stdscr.addstr(y_axis - 2, 0, "1: Incrypt")
                choose_crypt(stdscr, current_index, y_axis - 1)
            if key == curses.KEY_ENTER:
                stdscr.addstr(10, 10, "pressed enter")
                menu = False
        stdscr.attron(curses.color_pair(user_input_color))
        stdscr.get_wch(y_axis, 0)
        stdscr.attron(curses.color_pair(machine_color))
        y_axis += 1
        slow('Skriv besked: ', y_axis, stdscr)
        stdscr.attron(curses.color_pair(user_input_color))
        stdscr.getstr(y_axis, len('skriv besked: '))
        y_axis += 1
        # her printer den den krypterede eller dekrypterede beskede
        stdscr.attron(curses.color_pair(4))
        slow('(her skal koden stå)', y_axis, stdscr)
        y_axis += 1



curses.wrapper(main)