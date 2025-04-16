
# Personal PySide6 Project

This project skeleton provides a foundation for developing PySide6 applications. 
It is structured to streamline the workflow of using 'designer.exe', a WYSIWYG (What You See Is What You Get) GUI tool for generating Python UI scripts.

## Workflow Overview

- Open 'designer' and create the UI.
- Generate a Python UI script from the `.ui` file.
- Import the generated 'ui_example.py' into your application window class.
- Replace the contents of README.md to reflect your new project.
- Remove the skeleton .git repository and re-initialize Git for your project.

## Detailed Process

The 'designer' executable can be located in:

- `.venv\Scripts\pyside7-designer.exe`
- `.venv\Lib\site-packages\PySide6\designer.exe`

Choose the executable that suits your preference. 
Once your GUI design is complete, save it as a `.ui` file. Compile the `.ui` file into a Python script using the 'designer'. 
To do this, navigate to `Form > View Python Code` and save the resulting script in `gui\` folder which is in this project skeleton.

Once ui python script is made (ui_exmaple.py), you import this script into your main.py file.
See the following code example for the import.

```python

import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from gui.ui_example import Ui_MainWindow # change module name to your ui python script

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self): 
        super(MyWindow, self).__init__()
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
```
