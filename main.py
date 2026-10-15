from shutil import get_terminal_size
from sys import stdout

TERM_SIZE = get_terminal_size()
TERM_WIDTH = TERM_SIZE[0]
TERM_HEIGHT = TERM_SIZE[1]

FULL_CHAR = "█"

lines = "\n".join([FULL_CHAR * TERM_WIDTH for i in range(TERM_HEIGHT)])
stdout.write(f"\033[0;97m{lines}\033[0m")
input()