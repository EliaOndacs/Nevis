from xmlrpc.server import SimpleXMLRPCServer
from lib.Win20.win20 import *  # pack: ignore
from os import get_terminal_size
from ansi.cursor import goto
from ansi.iterm import image
from ansi.colour import fg, bg
from src.keyboard import getch # pack: ignore
import sys



def main(argv):

    if len(argv) <= 1:
        print("Usage: nevis [PORT] [ADDR?]")
        return
    if len(argv) == 2:
        port = int(argv[1])
        addr = "localhost"
    if len(argv) >= 3:
        addr = argv[1]
        port = int(argv[2])

    tw, th = get_terminal_size()
    MainWindow = Window(WinClass(tw, th))

    server = SimpleXMLRPCServer((addr, port), allow_none=True)

    def write(
        x,
        y,
        text,
        color: tuple[int, int, int] = (255, 255, 255),
        background: tuple[int, int, int] = (0, 0, 0),
    ):
        MainWindow.canvas.addstr(
            x, y, bg.truecolor(*background) + (fg.truecolor(*color) + text)
        )

    server.register_function(write)

    def clear_screen():
        print("\x1b[H\x1b[2J", end="")

    server.register_function(clear_screen)

    def clear_windows():
        MainWindow.clear()
        write(0, 0, "")

    server.register_function(clear_windows)

    def nevis_exit():
        sys.exit()

    server.register_function(nevis_exit)

    def Goto(x, y):
        print(goto(x, y), end="")

    server.register_function(Goto, "goto")

    def Image(filepath):
        print(image(filepath), end="")

    server.register_function(Image, "image")

    server.register_function(getch)

    render_count = 0

    clear_screen()
    try:
        while True:
            if render_count >= 3:
                try:
                    server.handle_request()
                except KeyboardInterrupt:
                    break
            else:
                write(0, 0, "")
            MainWindow.update()
            clear_screen()
            print(MainWindow, end="")
            render_count += 1
    finally:
        server.server_close()
        return


if __name__ == "__main__":
    main(sys.argv)
# end main
