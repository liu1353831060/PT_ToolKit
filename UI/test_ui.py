from PySide6.QtWidgets import QApplication,QWidget,QMainWindow,QMenu,QMenuBar
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction,QCursor
import sys
from UI_PT_ToolKit import Ui_MainWindow
from modules.ui_functions import UIFunctions

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.UI_init()

        #--信号连接
        self.ui.closeAppBtn.clicked.connect(self.on_closeWindow)
        self.ui.btn_wip.clicked.connect(self.on_buttonClick)
        self.ui.btn_cost.clicked.connect(self.on_buttonClick)
        self.ui.btn_scrap.clicked.connect(self.on_buttonClick)
        self.ui.btn_output.clicked.connect(self.on_buttonClick)
        self.ui.btn_database.clicked.connect(self.on_buttonClick)
        self.ui.btn_yield.clicked.connect(self.on_buttonClick)
        self.ui.btn_dashboard.clicked.connect(self.on_buttonClick)

        #---------------
    def on_buttonClick(self):
        btn = self.sender()
        btnName = btn.objectName()
        if btnName =="btn_wip":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_wip)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        if btnName =="btn_cost":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_cost)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        if btnName =="btn_scrap":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_scrap)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        if btnName =="btn_output":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_output)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        if btnName =="btn_database":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_database)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        if btnName =="btn_yield":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_yield)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
        if btnName =="btn_dashboard":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_dashboard)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))


    def UI_init(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Login)
        self.stackwidget_Contextmenu()

    def stackwidget_Contextmenu(self):
        self.menu = QMenu(self)
        action_delete = QAction("删除", self, triggered=self.handle_delete)
        self.menu.addAction(action_delete)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_menu)
    def show_menu(self, point):
        self.menu.exec(QCursor.pos())
        print('self ok')

    def handle_delete(self):
        print('is ok')

    def on_closeWindow(self):
        self.close()

    def mousePressEvent(self, event):  ##事件开始

        if Qt.LeftButton:
            self.Move = True  ##设定bool为True
            self.Point = event.globalPosition().toPoint() - self.pos()  ##记录起始点坐标
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):  ##移动时间
        if Qt.LeftButton and self.Move:  ##切记这里的条件不能写死，只要判断move和鼠标执行即可！
            self.move(QMouseEvent.globalPosition().toPoint() - self.Point)  ##移动到鼠标到达的坐标点！
            QMouseEvent.accept()
    def mouseReleaseEvent(self, QMouseEvent):  ##结束事件
        self.Move = False



if __name__ =='__main__':
    app = QApplication()
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec())
