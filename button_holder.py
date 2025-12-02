from PySide6.QtWidgets import QMainWindow, QPushButton

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Windonw 1")

        button = QPushButton("Press Me")
        button.setCheckable(True)
        val = button.isChecked()
        button.clicked.connect(self.button_clicked)

        self.setCentralWidget(button)

    def button_clicked(self, val):
        print("Button Pressed!",)