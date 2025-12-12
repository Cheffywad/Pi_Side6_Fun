from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout
import pyqtgraph
import numpy as np
from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QFont
from random import randint

class LiveGraph(QWidget):
    def __init__(self):
        super().__init__()

        self.graph1 = self.graph_setup('#FFFFFF', 'test', 'k','20pt', 'Times New Roman', '#000000', '14pt', 'xaxis', 'C', 'yaxis', 'K')
        self.graph2 = self.graph_setup('#FFFFFF', 'test', 'k','20pt', 'Times New Roman', '#000000', '14pt', 'xaxis', 'C', 'yaxis', 'K')

        self.time = [1,2,3,4,5,6,7,8,9,10]
        xarr = np.linspace(0, 4*np.pi, 100)
        yarr1 = np.sin(xarr)
        
        self.temperature = [30,32,34,32,33,31,29,32,35,45]

        self.graph1.addLegend()

        self.graph1.showGrid(x=True, y=True)
        self.graph2.showGrid(x=True, y=True)
        # # plot data: x, y values
        # self.graph1.setXRange(1, 10, padding=0.1)
        self.graph1.setYRange(30,45, padding=0.1)
        # self.graph2.setXRange(, 10, padding=0.1)
        self.graph2.setYRange(np.min(yarr1),np.max(yarr1), padding=0.05)

        penTemp = pyqtgraph.mkPen(color=(255, 0, 0), width=2, style=QtCore.Qt.DashLine)
        penHum = pyqtgraph.mkPen(color=(255, 0, 0), width=2, style=QtCore.Qt.DashLine)

        self.line1 = self.graph1.plot(self.time, self.temperature, name="Temperature", symbol='+', symbolSize=10, symbolBrush=('g'))
        self.line2 = self.graph2.plot(xarr, yarr1, name="Temperature")   
        
        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()
        h_layout.addWidget(self.graph1)
        h_layout.addWidget(self.graph2)
        self.setLayout(h_layout)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.plot_update_rand)
        self.timer.timeout.connect(self.numpy_graph_update(xarr, yarr1))
        self.timer.start()

    def numpy_graph_update(self, xarr, yarr):
        xarr_diff = np.average(np.diff(xarr))

        xarr_new_val = xarr_diff+xarr[-1]
        yarr_new_val = np.sin(xarr_new_val)

        xarr = np.append(xarr, xarr_new_val)
        yarr = np.append(yarr, yarr_new_val)

        xarr = np.delete(xarr, 0)
        yarr = np.delete(yarr, 0)

        self.line2.setData(xarr, yarr)

    def plot_update_rand(self):
        self.time = self.time[1:]
        self.time.append(self.time[-1] + 1)
        self.temperature = self.temperature[1:]
        self.temperature.append(randint(30, 40))
        self.line1.setData(self.time, self.temperature)

    def graph_setup(self, 
                graph_color:str, graph_title:str, 
                title_color:str, title_size:str, 
                label_font:str, label_color:str, label_size:str,
                xaxis_title:str, xaxis_unit:str,
                yaxis_title:str, yaxis_unit:str):
        self.graphWidget = pyqtgraph.PlotWidget()
        self.graphWidget.setBackground(graph_color)
        self.graphWidget.setTitle(graph_title, color=title_color, size=title_size)

        font = QFont(label_font)
        styles  = {'color': label_color, 'font-size': label_size}

        self.graphWidget.setLabel('bottom', xaxis_title, units=xaxis_unit, **styles)
        self.graphWidget.getAxis("bottom").label.setFont(font)
        self.graphWidget.setLabel('left', yaxis_title, units=yaxis_unit, **styles)

        return self.graphWidget
        