import sys
from PySide2 import QtWidgets as QtGui
from nptdms import TdmsFile
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np
import random

class Window(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # a figure instance to plot on
        self.figure = Figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas1 = FigureCanvas(self.figure)
        self.canvas2 = FigureCanvas(self.figure)
        self.canvas3 = FigureCanvas(self.figure)
        self.canvas4 = FigureCanvas(self.figure)
        self.canvas5 = FigureCanvas(self.figure)
        self.canvas6 = FigureCanvas(self.figure)
        self.canvas7 = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar1 = NavigationToolbar(self.canvas1, self)
        self.toolbar2 = NavigationToolbar(self.canvas2, self)
        self.toolbar3 = NavigationToolbar(self.canvas3, self)
        self.toolbar4 = NavigationToolbar(self.canvas4, self)
        self.toolbar5 = NavigationToolbar(self.canvas5, self)
        self.toolbar6 = NavigationToolbar(self.canvas6, self)
        self.toolbar7 = NavigationToolbar(self.canvas7, self)

        # Just some button connected to `plot` method
        self.button = QtGui.QPushButton('Plot')
        self.button.clicked.connect(self.plot)

        # set the layout
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.toolbar1)
        layout.addWidget(self.canvas1)
        layout.addWidget(self.toolbar2)
        layout.addWidget(self.canvas2)
        layout.addWidget(self.toolbar3)
        layout.addWidget(self.canvas3)
        layout.addWidget(self.toolbar4)
        layout.addWidget(self.canvas4)
        layout.addWidget(self.toolbar5)
        layout.addWidget(self.canvas5)
        layout.addWidget(self.toolbar6)
        layout.addWidget(self.canvas6)
        layout.addWidget(self.toolbar7)
        layout.addWidget(self.canvas7)

        layout.addWidget(self.button)
        self.setLayout(layout)

    def plot(self):
        ''' plot some random stuff '''
        # random data
        # data = [random.random() for i in range(10)]
        # tdms data

        tdms_file = TdmsFile("t1.tdms")

        tdms_groups = tdms_file.groups()
        data_array = []
        for grp in tdms_groups:
            for ch in reversed(tdms_file.group_channels(grp)):
                temp = str(ch).split('\'')
                # print((temp[1]), (temp[3]), ch)
                temp_obj = tdms_file.object(temp[1], temp[3])
                data_array.append(temp_obj.data)
                # ax = self.figure.add_subplot()
                # ax.clear()
                # ax.plot(temp_obj.data)
                # # getattr(self, "self.canvas%s.draw" % str(len(data_array)))()
                # self.canvas1.draw()
        data_array = np.asarray(data_array)

        ax1 = self.figure.add_subplot()
        ax1.clear()
        ax1.plot(data_array[0])
        self.canvas1.draw()

        ax2 = self.figure.add_subplot()
        ax2.clear()
        ax2.plot(data_array[1])
        self.canvas2.draw()

        ax3 = self.figure.add_subplot()
        ax3.clear()
        ax3.plot(data_array[2])
        self.canvas3.draw()

        ax4 = self.figure.add_subplot()
        ax4.clear()
        ax4.plot(data_array[3])
        self.canvas4.draw()

        ax5 = self.figure.add_subplot()
        ax5.clear()
        ax5.plot(data_array[4])
        self.canvas5.draw()

        ax6 = self.figure.add_subplot()
        ax6.clear()
        ax6.plot(data_array[5])
        self.canvas6.draw()

        ax7 = self.figure.add_subplot()
        ax7.clear()
        ax7.plot(data_array[6])
        self.canvas7.draw()

        # self.canvas1.draw()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    main = Window()
    main.resize(1920, 1010)
    main.show()

    sys.exit(app.exec_())