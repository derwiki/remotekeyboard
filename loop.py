#!/usr/bin/python

import os
import curses
import curses.ascii

DEBUG = False

command_mapping = {
	curses.KEY_LEFT:'Left',
	curses.KEY_RIGHT:'Right',
	curses.KEY_DOWN:'Down',
	curses.KEY_UP:'Up',
	#curses.KEY_ENTER:'Return',
	curses.ascii.ESC:'Escape',
	10:'Return',
	ord('('):'ParenLeft',
	ord(')'):'ParenRight',
	ord(' '):'Space',
}

try:
	stdscr = curses.initscr()
	stdscr.keypad(1)
	if DEBUG:
		curses.echo()
	while True:
		cmd = stdscr.getch()
		if cmd in command_mapping:
			cmd = command_mapping[cmd]
		else:
			stdscr.addstr("X: '%s'\n" % cmd)
			cmd = chr(cmd)
		if DEBUG:
			stdscr.addstr("xdotool key %s" % cmd)
		else:
			os.system("xdotool key %s" % cmd)
except KeyboardInterrupt, ki:
	print "Exiting..."
finally:
	curses.nocbreak()
	stdscr.keypad(0)
	curses.echo()
	curses.endwin()
