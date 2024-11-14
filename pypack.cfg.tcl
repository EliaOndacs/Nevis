
set-output "build/nevis.py"

# for better errors
packadd "lib/bsui_excepthook.py"
# BaseUi and a great theme for its components 
packadd "lib/BaseUiThemes.py" 
packadd "lib/BaseUi.py"

# Win20
packadd "lib/Win20/BaseUiVdom.py"
packadd "lib/Win20/win20.py" 

#local files
packadd "src/keyboard.py"

# main()
packadd "main.py"

