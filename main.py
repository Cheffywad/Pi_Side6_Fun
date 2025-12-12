import sys
from PySide6.QtWidgets import QApplication

# from main_window import MainWindow
# from button_clicking import ButtonClicking
# from text_editor import TextEditor
from live_graph import LiveGraph

app = QApplication(sys.argv)

widget = LiveGraph()
widget.show()

app.exec()



# from PySide6.QtCore import Qt
# from PySide6.QtWidgets import QApplication, QSlider

# def response_to_slider(data):
#     print("Slider moved to : ", data)

# app = QApplication()
# slider = QSlider(Qt.Horizontal)
# slider.setMinimum(1)
# slider.setMaximum(100)
# slider.setValue(25) 

# slider.valueChanged.connect(response_to_slider)
# slider.show()
# app.exec()