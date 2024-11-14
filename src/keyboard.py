import sys

WINDOWS = sys.platform == "win32"


def getch() -> bytes: ...


if WINDOWS:
    from msvcrt import getch
else:
    import tty
    import termios

    def getch() -> bytes:
        # Get the current terminal settings
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            # Set terminal to raw mode
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)  # Read a single character
        finally:
            # Restore the original terminal settings
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
