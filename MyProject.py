# Работа с формачками
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QFileDialog, QListWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore

#
import qimage2ndarray
import os
import sys
import cv2
import numpy as np

tasks = ["задание1", "задание2", "задание3"]

#  Главная форма
class Ui(QtWidgets.QMainWindow):
    def __init__(self, parent =None):
        super(Ui, self).__init__(parent)
        uic.loadUi('untitled.ui', self)

        self.window2 = Ui2()
        self.data = self.window2.data
        # календарь
    #    self.CalendarWidget.selectionChanged.connect(self.data_changed)
        self.AddTask.clicked.connect(self.add_task)
        self.DeleteTask_pushButton.clicked.connect(self.delete_task)
        self.window2.update_data.connect(self.update_list)
    #def data_changed(self):
    #    self.data = self.CalendarWidget.selectedDate().toPyDate()
    #    print(self.data)
    #    self.update_list()

    def update_list(self):
        self.listWidget.clear()
        for task in self.data:
            item = QListWidgetItem(task)
            self.listWidget.addItem(item)

    def add_task(self):
        self.window2.show()

    def delete_task(self):
        items = self.listWidget.selectedItems()
        if not items: return
        for item in items:
            self.listWidget.takeItem(self.listWidget.row(item))
            print(item)


# дочерняя
class Ui2(QtWidgets.QWidget):
    update_data = QtCore.pyqtSignal(list)
    def __init__(self, parent = None):
        super().__init__(parent)
        uic.loadUi('newTask.ui', self)
        self.data = []
        self.buttonBox.accepted.connect(self.get_new_task)

    def get_new_task(self):
        date = self.calendarWidget.selectedDate().toPyDate()
        time = self.timeEdit.time().toPyTime()
        task = self.textEdit.toPlainText()

        data = f"{date}" + '\n' + f"{time}" + '\n'+f"{task}"
        self.data.append(data)
        self.update_data.emit(self.data)
app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.show()
app.exec_()

