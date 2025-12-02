from PySide6.QtWidgets import QPushButton, QWidget, QHBoxLayout, QVBoxLayout

class RockeWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RocketWidget")

        button1 = QPushButton("Button 1")
        button1.clicked.connect(self.button1_clicked)

        button2 = QPushButton("Button 2")
        button2.clicked.connect(self.button2_clicked)

        button_layout = QVBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)

        self.setLayout(button_layout)

    def button1_clicked(self):
        print("Button1 clicked")

    def button2_clicked(self):
        print("Button2 clicked")

