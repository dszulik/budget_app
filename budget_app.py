from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import * 
import sys
from numpy import add
from pyqtgraph.graphicsItems.ROI import rectStr
from wykresy import rysujWykres
from pliczek import addReceipt
from tkinter import * 
import pyqtgraph as pg
from PyQt5.QtGui import *
from PyQt5.QtChart import  QChart, QChartView, QLineSeries, QCategoryAxis

class BarGraphItem(pg.BarGraphItem):

    def __init__(self, *args, **kwargs):
        pg.BarGraphItem.__init__(self, *args, **kwargs)
  
class Window(QMainWindow):
  
    def __init__(self):
        super().__init__()
        self.BudgetApp()
    
    def BudgetApp(self):
        self.setWindowTitle("Budget app")
        self.setGeometry(100, 100, 800, 500)
        self.BudgetChart()
       
        self.show()

    def BudgetChart(self):
        widget = QWidget()
        widget.setGeometry(120,120,300,200)
        plot = pg.plot()
        x,y,months = rysujWykres()

        bargraph = BarGraphItem(x = x, height = y, width = 0.6, brush ='b')
        plot.addItem(bargraph)

        layout = QGridLayout()
        widget.setLayout(layout)
        layout.addWidget(plot, 1, 1, 3, 1)
        button = QPushButton('Dodaj paragon', self)
        button.clicked.connect(addReceipt)
        button.clicked.connect(self.BudgetChart)
        button.move(100,50)
        layout.addWidget(button, 0, 1)
        self.setCentralWidget(widget)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())