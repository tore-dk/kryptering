#!/usr/bin/python3
import curses
import time


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
    current_row = 0
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    stdscr.attron(curses.color_pair(machine_color))
    # her starter den med at skrive
    slow('Giv din key', y_axis, stdscr)
    stdscr.attron(curses.color_pair(user_input_color))
    stdscr.getstr(1, 0)
    stdscr.clear()
    while True:
        stdscr.attron(curses.color_pair(machine_color))
        slow('1: Incrypt', y_axis, stdscr)
        y_axis += 1
        slow('2: Decrypt', y_axis, stdscr)
        y_axis += 1
        stdscr.attron(curses.color_pair(user_input_color))
        stdscr.get_wch(y_axis, 0)
        stdscr.attron(curses.color_pair(machine_color))
        y_axis += 1
        slow('Skriv besked: ', y_axis, stdscr)
        stdscr.attron(curses.color_pair(user_input_color))
        stdscr.getstr(y_axis, len('skriv besked: '))
        y_axis += 1
        # her printer den den krypterede eller dekrypterede beskede
        stdscr.attron(curses.color_pair())
        slow('(her skal koden stå)', y_axis, stdscr)
        y_axis += 1



curses.wrapper(main)