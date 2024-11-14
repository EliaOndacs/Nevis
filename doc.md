
# functions

write(x: int, y: int, text: str, color? : tuple[int, int int], background? : tuple[int, int int]) : write text at the x and y 

clear_screen() : refresh the screen
clear_windows() : remove everything on the screen and reset to a empty screen
goto(x: int, y: int) : move the cursor to x, y
image(filepath: str) : render an iterm protocol image
getch() : returns a bytes or an string of an captured key
