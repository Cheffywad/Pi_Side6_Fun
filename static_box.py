from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout
from PySide6.QtCore import QSize
from PySide6.QtGui import  QIcon

class StaticBox(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Message Boxes")
        
        button_hard = QPushButton("Hard")
        button_hard.clicked.connect(self.button_clicked_hard)

        button_crtical = QPushButton("Critical")
        button_crtical.clicked.connect(self.button_clicked_critical) 

        button_question = QPushButton("Question")
        button_question.clicked.connect(self.button_clicked_question)

        button_information = QPushButton("Information")
        button_information.clicked.connect(self.button_clicked_information)

        button_warning = QPushButton("Warning")
        button_warning.clicked.connect(self.button_clicked_warning)

        button_about = QPushButton("About")
        button_about.clicked.connect(self.button_clicked_about)

        button1 = QPushButton("RED BUTTON")
        button1.setIcon(QIcon("onshapelogo_critical.png"))
        button1.setIconSize(QSize(50,50))
        button1.clicked.connect(self.button1_clicked)

        message_layout = QVBoxLayout()
        message_layout.addWidget(button_hard)
        message_layout.addWidget(button_crtical)
        message_layout.addWidget(button_question)
        message_layout.addWidget(button_information)
        message_layout.addWidget(button_warning)
        message_layout.addWidget(button_about)

        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addLayout(message_layout)

        self.setLayout(layout)


    def button_clicked_hard(self):
        message = QMessageBox()
        message.setMinimumSize(700, 700)
        message.setWindowTitle("Hard")
        message.setText("Type Much")
        message.setInformativeText("This was hard")
        message.setIcon(QMessageBox.Critical)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)

        ret = message.exec()
        if ret == QMessageBox.Ok: 
            print("Coped")
        else:
            print("Lacking Cope")
    
    def button_clicked_critical(self):
        ret = QMessageBox.critical(self, "Message Title", "Critical Message!", QMessageBox.Ok | QMessageBox.Cancel)

        if ret == QMessageBox.Ok: 
            print("Coped")
        else:
            print("Lacking Cope")
        

    def button_clicked_question(self):
        ret = QMessageBox.question(self, "Message Title", "What", QMessageBox.Ok | QMessageBox.Cancel)

        if ret == QMessageBox.Ok: 
            print("Coped")
        else:
            print("Lacking Cope")

    def button_clicked_information(self):
        ret = QMessageBox.information(self,"Message Title",
                                        "Some information",
                                        QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok : 
            print("User chose OK")
        else : 
            print ("User chose Cancel")

    def button_clicked_warning(self):
        ret = QMessageBox.warning(self,"Message Title",
                                        "Some Warning",
                                        QMessageBox.Ok | QMessageBox.Cancel)
        if ret == QMessageBox.Ok : 
            print("User chose OK")
        else : 
            print ("User chose Cancel")

    def button_clicked_about(self):
        ret = QMessageBox.about(self,"Message Title",
                                        "Some about message")
        if ret == QMessageBox.Ok : 
            print("User chose OK")
        else : 
            print ("User chose Cancel")
    
    def button1_clicked(self):
        print("Opps")

    
    
    
    
