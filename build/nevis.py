"""
**BaseUi Exception Hook**

import this module to get beautiful error messages
by BaseUi.py

> Note:
> using this module dosen't require importing/packing BaseUi

"""

from typing import Any
from ansi.colour import *  # type: ignore
import sys
from types import TracebackType
from pathlib import Path
from os import get_terminal_size
tw, _ = get_terminal_size()


import pygments
from pygments.lexers import python
from pygments.formatters import TerminalFormatter

class Style:
    def __init__(self, **options: dict[str, Any]):
        self.__data__: dict[str, Any] = options
        self.get = self.__data__.get

    def __repr__(self):
        return f"[object of 'Style' id: {hex(id(self))!r} size: {self.__sizeof__()!r}]"

    def __setitem__(self, key, value):
        self.__data__[key] = value

    def __getitem__(self, key):
        return self.__data__[key]


def ascii_border(text, style: Style | None = None):
    lines = text.split("\n")
    max_len = max(len(line) for line in lines)
    if style:
        border_char = style.get("ascii_border", "-")
        border_vertical_char = style.get("border_vertical_char", "|")
    else:
        border_char = "-"
        border_vertical_char = "|"
    border = border_char * (max_len + 4)
    result = []
    for line in lines:
        bordered_line = (
            f"{border_vertical_char} {line.ljust(max_len)} {border_vertical_char}"
        )
        result.append(bordered_line)
    result.insert(0, border)
    result.append(border)
    return "\n".join(result)


class PrettyLogging:
    def error(self, name, detail, use_stdout: bool = False):
        text = fg.red("ERROR") + " -> " + fg.cyan(name) + ": " + fg.gray(detail)
        if use_stdout == True:
            print(text)
            return
        sys.stderr.write(text + "\n")
        sys.stderr.flush()

    def warn(self, name, detail, use_stdout: bool = False):
        text = fg.yellow("WARN") + " -> " + fg.cyan(name) + ": " + fg.gray(detail)
        if use_stdout == True:
            print(text)
            return
        sys.stderr.write(text + "\n")
        sys.stderr.flush()

    def info(self, name, detail, use_stdout: bool = False):
        text = fg.blue("INFO") + " -> " + fg.cyan(name) + ": " + fg.gray(detail)
        if use_stdout == True:
            print(text)
            return
        sys.stderr.write(text + "\n")
        sys.stderr.flush()


def get_logger() -> PrettyLogging:
    if "global_logger" not in globals():
        globals()["global_logger"] = PrettyLogging()
        return globals()["global_logger"]
    else:
        return globals()["global_logger"]


def bsui_excepthook(
    _type: type[BaseException], err: BaseException, trace: TracebackType | None
):
    def show_trace(trace: TracebackType | None):
        if trace != None:
            print(f"lineN:{trace.tb_lineno}")
            lines = Path(trace.tb_frame.f_code.co_filename).read_text().splitlines()
            new = ""
            i = 0
            for line in lines:
                if i >= (trace.tb_lineno - 5) and i <= (trace.tb_lineno + 5):
                    line = pygments.highlight(line, python.PythonLexer(), TerminalFormatter())
                    if i + 1 == trace.tb_lineno:
                        new += f"-> {i+1}|" + line
                    else:
                        new += f"   {i+1}|" + line
                i += 1
            print("-"*tw)
            print(new)
            print("-"*tw)
            if trace.tb_next != None:
                show_trace(trace.tb_next)

    show_trace(trace)
    get_logger().error(f"[{_type.__name__}]", repr(err))


sys.excepthook = bsui_excepthook
from typing import Any
from ansi.colour import fg

#simulate [copy and paste] BaseUi `Style` object 
class Style:
    def __init__(self, options: dict[str, Any]):
        self.__data__: dict[str, Any] = options
        self.get = self.__data__.get

    def __repr__(self):
        return f"[object of 'Style' id: {hex(id(self))!r} size: {self.__sizeof__()!r}]"

    def __setitem__(self, key, value):
        self.__data__[key] = value

    def __getitem__(self, key):
        return self.__data__[key]

smooth_cute = Style({
    'ascii_border': '─',
    'border_vertical_char': '│',
    'ProgressBar.left': '[',
    'ProgressBar.right': ']',
    'ProgressBar.tip': '>',
    'ProgressBar.lineOff': ' ',
    'ProgressBar.lineOn': '=',
    'ProgressBar.color:on': fg.yellow,
    'DataTable.seperator': '│',
    'DataTable.right': '│',
    'DataTable.left': '│',
    'Bar.seperator': ':',
    'Chain.left': '{',
    'Chain.right': '}',
    'Chain.seperator': '~',
    'Ruler.begin': '/',
    'Ruler.end': '>',
    'Ruler.line': '-',
    'List.override_index': True,
    'Compersition.not_equal': '!=',
    'Notification.left': '(',
    'Notification.right': ')',
})


# note: this requires nerdfont
so_nerdy = Style({
    'ProgressBar.left': '\uf104',
    'ProgressBar.right': ' \uf105',
    'ProgressBar.tip': ' \ueabc',
    'ProgressBar.lineOff': '\uf45b',
    'ProgressBar.lineOn': '\uf45b',
    'ProgressBar.color:on': fg.magenta,
    'DataTable.seperator': '\udb84\udef1',
    'DataTable.right': '\udb84\udef1',
    'DataTable.left': '\udb84\udef1',
    'Bar.seperator': '\uf142',
    'Chain.left': '\ue0b7',
    'Chain.right': '\ue0b5',
    'Chain.seperator': '-',
    'Ruler.begin': '\ue0b6',
    'Ruler.end': '>',
    'Ruler.line': '-',
    'List.override_index': True,
    'Compersition.not_equal': '!=',
    'Notification.left': '\uf12a\ue0b7',
    'Notification.right': '\ue0b5',
})

minimal_space = Style({
    "ascii_border": '.',
    "border_vertical_char": ':',
    "ProgressBar.left": ' ',
    "ProgressBar.right": ' ',
    "ProgressBar.tip": '>',
    "ProgressBar.lineOn": '-',
    "ProgressBar.lineOff": ' ',
    "ProgressBar.color:on": fg.grey,
    "DataTable.seperator": ' : ',
    "DataTable.left": ' ',
    "DataTable.right": ' ',
    "Bar.seperator": '%',
    "Chain.left": " ",
    "Chain.right": " ",
    "Chain.seperator": "-",
    "Select.promptText": ':',
    "Ruler.begin": " ",
    "Ruler.end": ">",
    "Ruler.line": "-",
    "Mark.off": " ",
    "Mark.on": "*",
    "Compersition.not_equal": "!=",
    "Notification.left": "|",
    "Notification.right": "|",
    "ImportanceText.fg": fg.red,
    "Paginator.left": " ",
    "Paginator.right": " ",
    "Input.promptText": ": "
})

"""
**BaseUi**

the base ui library for a centerlised theme cli ui among SysCoreutil & SysEnv

"""

from typing import (
    Any,
    Generator,
    Iterable,
    Literal,
    NamedTuple,
)
from warnings import deprecated
from ansi.colour import *  # type: ignore
import sys


class Style:
    "style object for all styles of all components"

    def __init__(self, options: dict[str, Any]):
        self.__data__: dict[str, Any] = options
        self.get = self.__data__.get

    def __repr__(self):
        return f"[object of 'Style' id: {hex(id(self))!r} size: {self.__sizeof__()!r}]"

    def __setitem__(self, key, value):
        self.__data__[key] = value

    def __getitem__(self, key):
        return self.__data__[key]


AT_STYLE = "Style"
AT_DISPLAY = "Display"


def make_auto(_type, instance):
    "turn an object to an auto object"
    if _type == "Style":
        globals()["@auto[style]"] = instance
        return
    elif _type == "Display":
        globals()["@auto[display]"] = instance
        return

    raise TypeError(f"type {_type!r} it not supported as an auto object!")


def get_style(style: Style | None):
    "get the the aut style if exsist or None or the past style pram"
    if style:
        return style
    if "@auto[style]" in globals():
        return globals()["@auto[style]"]


class Animation:
    "Base Object For All Animations"

    class Frame:
        def __init__(self, text: str) -> None:
            self.text: str = text

    @classmethod
    def FramesFromList(cls, frames: list[Any]) -> list["Animation.Frame"]:
        result = []
        for frame in frames:
            result.append(Animation.Frame(str(frame)))

        return result

    def __init__(self, frames: list["Animation.Frame"]) -> None:
        self.frames = frames
        self.frameI = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.frameI += 1

    def __str__(self) -> str:
        return self.frames[self.frameI % len(self.frames)].text


class Measurements(NamedTuple):
    """Measurements of an text"""

    columns: int
    lines: int
    text: str

    @classmethod
    def measure(cls, text: str):
        "measure a text"
        l = text.split("\n")
        max_columns = len(max(l, key=len))
        return Measurements(max_columns, len(l), text)


class Block:
    """A Block Of Text (a multiline text)"""

    def __init__(self, raw: str) -> None:
        self._raw = raw  # very unsafe, but might be required later
        self.measurments = Measurements.measure(self._raw)
        self.text: list[str] = self._raw.split("\n")

    def render(self) -> Generator[str, None, None]:
        for line in self.text:
            yield line

    def __str__(self) -> str:
        return "\n".join(self.text)

def deleteText(text: str):
    return "\b"*len(text)

def ascii_border(text, style: Style | None = None):
    "make an ascii border around the `text`"
    style = get_style(style)
    lines = text.split("\n")
    max_len = max(len(line) for line in lines)
    if style:
        border_char = style.get("ascii_border", "-")
        border_vertical_char = style.get("border_vertical_char", "|")
    else:
        border_char = "-"
        border_vertical_char = "|"
    border = border_char * (max_len + 2)
    result = []
    for line in lines:
        bordered_line = (
            f"{border_vertical_char}{line.ljust(max_len)}{border_vertical_char}"
        )
        result.append(bordered_line)
    result.insert(0, border)
    result.append(border)
    return "\n".join(result)


def VerticalLabel(text: str):
    return "\n".join(list(text))


class ProgressBar:
    "ProgressBar Component"

    def __init__(
        self,
        default: int = 0,
        max: int = 100,
        size: int = 10,
        style: Style | None = None,
    ) -> None:
        self.value = default
        self.max = max
        self.style = get_style(style)
        self.size = size

    def update(self, ammount: int = 1):
        self.value += ammount

    def reset(self):
        self.value = 0

    def __str__(self):
        result = ""
        if self.style:
            left = self.style.get("ProgressBar.left", "<")
            right = self.style.get("ProgressBar.right", ">")
            tip = self.style.get("ProgressBar.tip", "o")
            line_off = self.style.get("ProgressBar.lineOff", "-")
            line_on = self.style.get("ProgressBar.lineOn", "-")
            on_color = self.style.get("ProgressBar.color:on", fg.cyan)
            off_color = self.style.get("ProgressBar.color:off", fg.grey)
        else:
            left = "<"
            right = ">"
            tip = "o"
            line_on = "-"
            line_off = "-"
            on_color = fg.cyan
            off_color = fg.grey
        ammount_filled: int = self.value * self.size // self.max
        for i in range(ammount_filled):
            result += (
                (on_color + tip) if i == (ammount_filled - 1) else (on_color + line_on)
            )
        result += (off_color + line_off) * (self.size - ammount_filled)

        return f"{left}{result}{right}\x1b[0m"


class Spinner:
    "Spiner Component (Composition `Animation` object with an default animation)"

    def _get_default_animation(self) -> Animation:
        return Animation(
            Animation.FramesFromList(["|", "/", "─", "\\", "|", "/", "─", "\\"])
        )

    def __init__(self, animation: None | Animation = None) -> None:
        self.animation: "Animation" = animation if animation != None else self._get_default_animation  # type: ignore

    def __iter__(self):
        return self

    def __next__(self):
        next(self.animation)

    def __str__(self):
        return str(self.animation)


class DataTable:
    "DataTable component"

    class Column:
        "A Column Object For DataTable.Row"

        def __init__(self, text: str) -> None:
            self.text = text

        def __str__(self):
            return self.text

    class Row:
        "A Row Object for DataTable"

        def __init__(self, *cols) -> None:
            self.cols = cols

    def __init__(self, style: Style | None = None) -> None:
        self.data: list["DataTable.Row"] = []
        self.style = get_style(style)

    def add_row(self, row: "DataTable.Row"):
        self.data.append(row)

    def __str__(self):
        result = ""

        if self.style:
            seperator = self.style.get("DataTable.seperator", "|")
            left = self.style.get("DataTable.left", "[")
            right = self.style.get("DataTable.right", "]")
        else:
            seperator = "|"
            left = "["
            right = "]"

        for row in self.data:
            items = []
            for item in row.cols:
                items.append(str(item))

            result += f"{left}{f'{seperator}'.join(items)}{right}\n"

        return result


class Padding:
    "Adds Padding For strings"

    @classmethod
    def left(cls, text: str, amount: int = 5):
        return (" " * amount) + text

    @classmethod
    def right(cls, text: str, amount: int = 5):
        return text + (" " * amount)

    @classmethod
    def center(cls, text: str, Amount: int = 5):
        return Padding.left(Padding.right(text, amount=Amount), amount=Amount)

    @classmethod
    def up(cls, text: str, amount: int = 1):
        return ((" " * len(text) + "\n") * amount) + text

    @classmethod
    def down(cls, text: str, amount: int = 1):
        return text + ((" " * len(text) + "\n") * amount)

    @classmethod
    def middle(cls, text: str, amount: int = 1):
        return Padding.down(Padding.up(text, amount=amount), amount=amount)

    @classmethod
    def complete(cls, text: str, amount: tuple[int, int] = (5, 1)):
        return Padding.middle(Padding.center(text, Amount=amount[0]), amount=amount[1])


class SwitchText:
    "SwitchText Atomic, allow you to switch between text on render"

    def __init__(self, text_a: str, text_b: str):
        self.text_a = text_a
        self.text_b = text_b
        self.switch: Literal[0, 1] = 0

    def __str__(self):
        return self.text_a if self.switch == 0 else self.text_b

    def alternate(self):
        if self.switch == 0:
            self.switch = 1
        else:
            self.switch = 0

    def update(self, text: str):
        if self.switch == 0:
            self.text_a = text
        else:
            self.text_b = text


class Input:
    "Input Component (Only Fires When Try To Convert To A String And Will Return The UserInput)"

    def __init__(self, prompt: str = "", style: Style|None = None):
        self.prompt = prompt
        self.style = get_style(style)

    def __str__(self):
        if self.style:
            prompt = self.style.get("Input.promptText", "")
        else:
            prompt = ""
        return input(prompt)


class Title:
    "Title Desighn"

    def __init__(self, text: str):
        self.text = f"-[{text}]-"

    def __str__(self):
        return self.text


class Bar:
    "Bar Seperates Multiple Items In One Line"

    def __init__(self, *cols, style: Style | None = None, active: int|None = None) -> None:
        self.cols = cols
        self.active = active
        self.style = get_style(style)

    def __str__(self):
        if self.style:
            sep = self.style.get("Bar.seperator", ">")
        else:
            sep = ">"
        if self.active and len(self.cols) <= self.active:
            self.cols = list(self.cols)
            self.cols[self.active] = fx.underline(self.cols[self.active])
        return f" {sep} ".join(self.cols)


class Icon:
    "Icon Desighn, An Icon For Diffrent Names"

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self):
        return f"</{self.name.capitalize()}>"


class Chain:
    "Chain Desighn, A Chain For A Chain Of Values"

    def __init__(self, *cols, style: Style | None = None):
        self.cols = cols
        self.style = get_style(style)

    def __str__(self):
        result = ""

        if self.style:
            left = self.style.get("Chain.left", "(")
            right = self.style.get("Chain.right", ")")
            sep = self.style.get("Chain.seperator", "-")
        else:
            left = "("
            right = ")"
            sep = "-"

        for item in self.cols:
            result += f"{left}{item}{right}{sep}"

        return result[:-1]


class PrettyLogging:
    "Pretty Logging"

    def error(self, name, detail, use_stdout: bool = False):
        text = fg.red("ERROR") + " -> " + fg.cyan(name) + ": " + fg.gray(detail)
        if use_stdout == True:
            print(text)
            return
        sys.stderr.write(text + "\n")
        sys.stderr.flush()

    def warn(self, name, detail, use_stdout: bool = False):
        text = fg.yellow("WARN") + " -> " + fg.cyan(name) + ": " + fg.gray(detail)
        if use_stdout == True:
            print(text)
            return
        sys.stderr.write(text + "\n")
        sys.stderr.flush()

    def info(self, name, detail, use_stdout: bool = False):
        text = fg.blue("INFO") + " -> " + fg.cyan(name) + ": " + fg.gray(detail)
        if use_stdout == True:
            print(text)
            return
        sys.stderr.write(text + "\n")
        sys.stderr.flush()


def get_logger() -> PrettyLogging:
    "if `global_logger` exsist it will just return ir, if not it will create and then remove it"
    if "global_logger" not in globals():
        globals()["global_logger"] = PrettyLogging()
        return globals()["global_logger"]
    else:
        return globals()["global_logger"]


class Pointer:
    "Four Directional Pointer Desighn"
    left: str = " "
    right: str = " "
    up: str = " "
    down: str = " "


def join_string(*objs: str):
    "joins multiple string by space"
    return " ".join(objs)


class Select:
    "MultiChoice Menu (Composition DataTable)"

    def __init__(self, choices: list[str], style: Style | None = None) -> None:
        self.dt = DataTable(style)
        self.choices = choices
        self.style = get_style(style)
        i = 0
        for choice in choices:
            self.dt.add_row(
                DataTable.Row(DataTable.Column(str(i)), DataTable.Column(choice))
            )
            i += 1

    def __str__(self):
        print(self.dt)
        while 1:
            if self.style:
                inp = input(self.style.get("Select.promptText", "> "))
            else:
                inp = input("> ")
            try:
                result = self.choices[int(inp)]
                break
            except KeyboardInterrupt:
                get_logger().info("Select", "Canceled By The User.")
                sys.exit(-1)
            except:
                get_logger().error(
                    "SelectionError",
                    "input value is not an number or out of range. try again",
                )

        return result  # type: ignore


class Br:
    "New Line Object"

    def __str__(self) -> str:
        return "\n"


class Ruler:
    "A Ruller Object that can display a length of numbers"

    def __init__(self, lenght: int, style: Style | None = None) -> None:
        self.lenght = lenght
        self.style = get_style(style)

    def __str__(self) -> str:
        result = ""

        if self.style:
            begin = self.style.get("Ruler.begin", "|")
            end = self.style.get("Ruler.end", ">")
            line = self.style.get("Ruler.line", "-")
            number_on_top: bool = self.style.get("Ruler.NumberOnTop?", False)
        else:
            begin = "|"
            end = ">"
            line = "-"
            number_on_top = False

        # the ruler it self

        if number_on_top == False:
            result += begin + (line * (self.lenght * 3)) + end + "\n"

        # the numbers

        for i in range(self.lenght + 1):
            result += str(i) + "  "
        result += "\n"

        if number_on_top == True:
            result += begin + (line * (self.lenght * 3)) + end + "\n"

        return result


# (4) point


class Mark:
    "A Mark For Behind A Text or An Option"
    _mode: bool
    _override_mode: None | tuple[str, str] = None

    def __init__(
        self, string: str, mode: bool = False, style: Style | None = None
    ) -> None:
        self.string = string
        self.style = get_style(style)
        self.mode = mode

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, new: bool):
        self._mode = new

    def __str__(self) -> str:
        if self.style:
            mark_on = self.style.get("Mark.on", "($)")
            mark_off = self.style.get("Mark.off", "( )")
        else:
            mark_on = "($)"
            mark_off = "( )"

        if self._override_mode:
            mark_on = self._override_mode[0]
            mark_off = self._override_mode[1]

        if self.mode:
            mark = mark_on
        else:
            mark = mark_off

        return f"{mark} {self.string}"


class List:
    "A List Displayt Of multiple items"

    def __init__(
        self, items: Iterable | list | tuple, style: Style | None = None
    ) -> None:
        self.style = get_style(style)
        self.items = items

    def __str__(self) -> str:
        result = ""
        if self.style:
            mode = self.style.get("List.Marker.mode", True)
        else:
            mode = True

        i = 0
        for item in self.items:
            m = Mark(item, mode, style=self.style)
            if self.style:
                if self.style.get("List.override_index", True):
                    m._override_mode = (f"{i}.", "undefined")
            result += f"{str(m)}\n"
            i += 1

        return result


class Compersition:
    "Show Relations between two object"

    def __init__(self, a, b, style: Style | None = None) -> None:
        self.a = a
        self.b = b
        self.style = get_style(style)

    def __str__(self):
        if self.style:
            not_equal = self.style.get("Compersition.not_equal", "<>")
        else:
            not_equal = "<>"
        result = ""
        if self.a == self.b:
            result += f"({self.a} == {self.b})" + " "
        if self.a != self.b:
            result += f"({self.a} {not_equal} {self.b})" + " "
        if self.a < self.b:
            result += f"({self.a} < {self.b})" + " "
        if self.a > self.b:
            result += f"({self.a} > {self.b})" + " "
        return result[:-1]


class Crop:
    "Adds Cropping to strings"

    @classmethod
    def line(cls, string: str, amount: int = 5, offset: int = 0):
        return string[offset:amount]

    @classmethod
    def text(
        cls,
        string: str,
        measurements: Measurements | None = None,
        amount: tuple[int, int] = (3, 5),
        offset: tuple[int, int] = (0, 0),
    ):
        if (
            measurements
        ):  # a lot of typing errors, but trust me, this works perfectly fine
            amount: list[int] = list(amount)
            amount[0] = measurements.lines
            amount[1] = measurements.columns
            amount: tuple[int, int] = tuple(amount)

        result = ""
        lines = string.splitlines()
        for li in range(len(string)):
            if li >= amount[0]:
                break
            if li + offset[0] >= len(lines):
                break
            result += Crop.line(lines[li + offset[0]], amount[1], offset[1]) + "\n"
            li += 1

        return result[:-1]


class Notification:
    "Notification Component"

    def __init__(
        self,
        message: str,
        severity: Literal["Error", "Info", "Warning"] | None = None,
        style: Style | None = None,
    ) -> None:
        self.message = message
        self.severity = severity
        self.style = get_style(style)

    def __str__(self):
        if self.style:
            err_bg = self.style.get("Notification.error_bg", bg.red)
            err_fg = self.style.get("Notification.error_fg", fg.black)
            info_bg = self.style.get("Notification.info_bg", bg.blue)
            info_fg = self.style.get("Notification.info_fg", fg.black)
            warn_bg = self.style.get("Notification.warn_bg", bg.yellow)
            warn_fg = self.style.get("Notification.warn_fg", fg.black)
            left = self.style.get("Notification.left", "[")
            right = self.style.get("Notification.right", "]")
            do_reset = self.style.get("Notification.reset", True)
        else:
            err_bg = bg.red
            err_fg = fg.black
            info_bg = bg.blue
            info_fg = fg.black
            warn_bg = bg.yellow
            warn_fg = fg.black
            left = "["
            right = "]"
            do_reset = True

        _bg = ""
        _fg = ""
        if self.severity != None:
            match self.severity:
                case "Error":
                    _bg = err_bg
                    _fg = err_fg
                case "Info":
                    _bg = info_bg
                    _fg = info_fg
                case "Warning":
                    _bg = warn_bg
                    _fg = warn_fg
        return f"{_bg}{_fg}{left}{self.message}{right}{'\x1b[0m' if do_reset else ''}"


def fill(text: str, desired_length: int, filler: str = " "):
    "fills the infront of the `text` with the `filler` to make the text the `desired_length`"
    if len(text) >= desired_length:
        return text
    amount = desired_length - len(text)
    return text + (filler * amount)


class Tree:
    "Tree Component"

    def __init__(self, items: list[str | list]) -> None:
        self.items = items

    def _visit_node(self, items: list[str | list], depth: int = 0):
        result = ""
        for item in items:
            if isinstance(item, str):
                result += "\n" + Padding.left(item, amount=(depth * 4))
            elif isinstance(item, list):
                result += Padding.left(self._visit_node(item, depth + 1))
        return result

    def __str__(self) -> str:
        return self._visit_node(self.items)


class Canvas:
    "Canavs Component"

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self._buffer: list[list[str]] = [
            [" " for __ in range(self.width)] for _ in range(self.height)
        ]

    def addstr(self, x: int, y: int, string: str):
        lines = string.split("\n")
        iy = 0
        for line in lines:
            self.addline(x, y + iy, line)
            iy += 1

    def addline(self, x: int, y: int, string: str):
        if len(string.split("\n")) > 1:
            raise ValueError(
                f"expected the string: {string!r}, would be only one line, found multiple instead!"
            )
        ix = 0
        for char in string:
            self.addpixel(x + ix, y, char)
            ix += 1

    def addpixel(self, x: int, y: int, char: str):
        if x >= self.width:
            x = x % self.width
        if x < 0:
            x = 0
        if y >= self.height:
            y = y % self.height
        self._buffer[y][x] = char

    def __str__(self) -> str:
        result = ""
        for row in self._buffer:
            for col in row:
                result += Canvas.RuleOneChar(col)
            result += "\n"
        return result

    @classmethod
    def RuleOneChar(cls, string: str):
        "strip a string to only one char"
        return string[0]


class ImportanceText:
    def __init__(self, messages: str, style: Style | None = None) -> None:
        self.messages = messages
        self.style = style

    def __str__(self) -> str:
        if self.style:
            wall_fg = self.style.get("ImportanceText.fg", fg.grey)
            wall_bg = self.style.get("ImportanceText.bg", "")
        else:
            wall_fg = fg.grey
            wall_bg = ""
        return (
            wall_fg
            + wall_bg
            + "{"
            + "\x1b[0m"
            + f" {self.messages} "
            + wall_fg
            + wall_bg
            + "}"
            + "\x1b[0m"
        )


class AnsiText:

    class Segment:
        def __init__(self, text: str, is_control: bool) -> None:
            self.text = text
            self.is_control = is_control

        def __len__(self):
            return len(self.text)

    def __init__(self, segments: list["AnsiText.Segment"]) -> None:
        self.segs = segments

    def __len__(self):
        result = 0
        for seg in self.segs:
            if seg.is_control:
                continue
            result += len(seg)
        return result

    def __str__(self):
        result = ""
        for seg in self.segs:
            result += seg.text
        return result


class FilesystemDeco:
    NormalFile = lambda filename: fg.yellow(filename)
    Directory = lambda filename: fg.blue(filename)
    Executable = lambda filename: fg.red(filename) + fg.grey("*")


class Paginator:
    def __init__(
        self,
        default_page: int = 1,
        amount_of_pages: int = 5,
        style: Style | None = None,
    ) -> None:
        self.pages: int = amount_of_pages
        self.pageN = default_page
        self.style = style

    def __str__(self):
        if self.style:
            left = self.style.get("Paginator.left", "[")
            right = self.style.get("Paginator.right", "]")
            active_page = self.style.get("Paginatio.active", "o")
            unactive_page = self.style.get("Paginator.unactive", ".")
        else:
            left = "["
            right = "]"
            active_page = "o"
            unactive_page = "."
        result = left
        for i in range(self.pages):
            if i == self.pageN:
                result += active_page
            else:
                result += unactive_page
        return result + right
from typing import Any


class DOMNode:
    _component: Any
    _attrs: dict[str, Any]

    def __init__(self, component, id: str, childs: list["DOMNode"] = [], **attrs):
        self.component = component
        self.childs = childs
        self.id = id
        self.attributes = attrs

    @property
    def attributes(self):
        return self._attrs

    @attributes.setter
    def attributes(self, new):
        self._attrs = new

    def setAttribute(self, attr: dict[str, Any]):
        self._attrs = {**self._attrs, **attr}

    @property
    def component(self):
        return self._component

    @component.setter
    def component(self, new: Any):
        self._component = new

    @component.deleter
    def component(self):
        del self._component

    def __str__(self):
        return str(self.component)

    def replaceWith(self, component):
        self.component = component

    def query(self, id: str):
        result = []
        for child in self.childs:
            if child.id == id:
                result.append(child)
            result.extend(child.query(id))
        return result

    def insertNode(self, node: "DOMNode"):
        self.childs.append(node)

    def render(self):
        result = ""
        for child in self.childs:
            result += str(child)
            result += child.render()
        return result


class DOM(DOMNode):
    def __init__(self, childs: list["DOMNode"] = []):
        super().__init__('', "$DOM", childs)

    def __str__(self):
        return self.render()
from enum import Enum, auto
from dataclasses import dataclass


class TextLayer:
    def compose(self) -> Generator[str | Any, None, None]:
        yield from ()

    def __str__(self) -> str:
        result = list(self.compose())
        final_result = map((lambda item: str(item)), result)
        return "".join(final_result)


class AnsiLayer:
    def compose(self) -> Generator[str, None, None]:
        yield from ()

    def __str__(self) -> str:
        final_result = list(self.compose())
        return "".join(map(str, final_result))


class IconLayer:
    def compose(self) -> Generator[str, None, None]:
        yield from ()

    def __str__(self) -> str:
        final_result = list(self.compose())
        return "".join(final_result)


type MediaLayer = TextLayer | AnsiLayer | IconLayer


class WinType(Enum):
    Normal = auto()
    Float = auto()
    Notification = auto()
    Segement = auto()


@dataclass()
class WinClass:
    width: int
    height: int
    Type: WinType = WinType.Normal


class Window:
    def __init__(self, Class: WinClass) -> None:
        self._winclass = Class
        self.canvas = Canvas(self._winclass.width, self._winclass.height)
        self.dom = DOM()

    def replaceLayer(self, id: str, replaceMedia: MediaLayer, **attributes):
        for node in self.dom.query(id):
            node.replaceWith(replaceMedia)
            node.setAttribute(attributes)

    def append(self, media: MediaLayer, id: str = "$None", **attributes):
        self.dom.insertNode(DOMNode(str(media), id, **attributes))

    def update(self):
        self.canvas.addstr(0, 0, str(self.dom))

    def clear(self):
        del self.canvas
        self.canvas = Canvas(self._winclass.width, self._winclass.height)

    def __str__(self):
        return str(self.canvas)
from xmlrpc.server import SimpleXMLRPCServer
from os import get_terminal_size
from ansi.cursor import goto
from ansi.iterm import image
from ansi.colour import fg, bg
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
