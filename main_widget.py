from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QTabWidget, QLabel
from pyqtgraph import PlotWidget

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        main_layout = QHBoxLayout()

        self.tab_widget = QTabWidget()
        self.control_tab = QWidget()
        self.data_tab = QWidget()
        self.graph_tab = QWidget()

        self.tab_widget.addTab(self.control_tab, 'Control')
        self.tab_widget.addTab(self.data_tab, "Data")
        self.tab_widget.addTab(self.graph_tab, "Graphs")
        main_layout.addWidget(self.tab_widget)
        
        self.controlTab()
        self.graphTab()

        self.setLayout(main_layout)

    def controlTab(self):

        label = QLabel("Control Tab Contents")
        button1 = QPushButton("Test")
        
        control_layout = QVBoxLayout(self.control_tab)
        control_layout.addWidget(button1)
        control_layout.addWidget(label)

    def graphTab(self):
        plot_1 = PlotWidget(name="Plot 1")
        plot_2 = PlotWidget(name="Plot 2")
        plot_3 = PlotWidget(name="Plot 3")
        plot_4 = PlotWidget(name="Plot 4")

        horz_layout_1 = QHBoxLayout()
        horz_layout_2 = QHBoxLayout()
        horz_layout_1.addWidget(plot_1)
        horz_layout_1.addWidget(plot_2)
        horz_layout_2.addWidget(plot_3)
        horz_layout_2.addWidget(plot_4)

        main_layout = QVBoxLayout(self.graph_tab)
        main_layout.addLayout(horz_layout_1)
        main_layout.addLayout(horz_layout_2)



