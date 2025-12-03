from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox, QLabel, QLineEdit, QHBoxLayout

class ButtonClicking(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lable and Edit")
        
        label = QLabel("Name : ")
        self.line_edit = QLineEdit()
        # self.line_edit.textChanged.connect(self.text_changed)
        # self.line_edit.cursorPositionChanged.connect(self.cursor_position_chnaged)        
        # self.line_edit.editingFinished.connect(self.editing_finished)
        # self.line_edit.returnPressed.connect(self.return_pressed)
        # self.line_edit.selectionChanged.connect(self.selection_changed)
        self.line_edit.textEdited.connect(self.text_edited)

        button = QPushButton("Get Data")
        button.clicked.connect(self.button_clicked)
        self.text_holder_label = QLabel("Here")

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder_label)

        self.setLayout(v_layout)

    def button_clicked(self):
        # print('Name : ', self.line_edit.text())
        self.text_holder_label.setText(self.line_edit.text()) 

    def text_changed(self):
        self.text_holder_label.setText(self.line_edit.text()) 

    def cursor_position_chnaged(self, old, new):
        print("Cursor old pos : ", old, "New pos : ", new)

    def editing_finished(self):
        print("Editing Finished")

    def return_pressed(self):
        print("Return pressed")

    def selection_changed(self):
        print("Selection changed : ", self.line_edit.selectedText())

    def text_edited(self, new_text):
        print("Text Edited...New Text : ", new_text)