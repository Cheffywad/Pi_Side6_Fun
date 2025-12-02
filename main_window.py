from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar, QHBoxLayout, QDockWidget
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from rock_widget import RockeWidget
from static_box import StaticBox


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Cusom Main Window")
        self.setGeometry(50, 50, 400, 400)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")

        quit_aqction = file_menu.addAction("Quit")
        quit_aqction.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        menu_bar.addMenu("Window")
        menu_bar.addMenu("Setting")
        menu_bar.addMenu("Help")

        toolbar = QToolBar("My toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        toolbar.addAction(quit_aqction)

        action1 = QAction("Action1", self)
        action1.setStatusTip("Action decription")
        action1.triggered.connect(self.toolbar_botton_click)
        toolbar.addAction(action1)

        action2 = QAction(QIcon("onshapelogo.png"), "Some action", self)
        action2.setStatusTip("Action 2 Status")
        action2.triggered.connect(self.toolbar_botton_click)
        # action2.setCheckable(True)
        toolbar.addAction(action2)

        toolbar.addSeparator()
        toolbar.addWidget(RockeWidget())

        self.setStatusBar(QStatusBar(self))

        # button1 = QPushButton("RED BUTTON")
        # button1.setIcon(QIcon("onshapelogo_critical.png"))
        # button1.setIconSize(QSize(50,50))
        # button1.clicked.connect(self.button1_clicked)
        self.setCentralWidget(StaticBox())

        # layout = QHBoxLayout()
        # layout.addWidget(button1)
        # layout.addWidget(StaticBox())
        # self.setLayout(layout)
 
    def quit_app(self):
        self.app.quit()

    def toolbar_botton_click(self):
        print("Action triggered")
        self.statusBar().showMessage("Message from app", 3000)

    # def button1_clicked(self):
    #     print("Opps")