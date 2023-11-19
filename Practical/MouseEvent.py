from PySide6.QtWidgets import QApplication,QWidget,QLineEdit
from PySide6.QtCore import Qt,QEvent
import sys

class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.resize(500,300)
        self.LineEdit = QLineEdit(self)
        self.LineEdit.setGeometry(0,0,500,30)
        #鼠标相关事件和函数对应
        #QEvent.MouseButtonPress -> mousePressEvent
        #QEvent.MouseButtonRelease -> mouseReleaseEvent
        #QEvent.MouseMove -> mouseMoveEvent
        #QEvent.MouseButtonDblClick -> mouseDoubleClickEvent
    def event(self,event:QEvent):
        if event.type() ==QEvent.MouseButtonPress:
            if event.button()==Qt.LeftButton:
                string = "窗口坐标x:{},y:{}".format(event.position().x(),event.position().y())
                self.LineEdit.setText(string)
            if event.button()==Qt.RightButton:
                string = "屏幕坐标x:{},y:{}".format(event.globalPosition().x(),event.globalPosition().y())
                self.LineEdit.setText(string)
            return True
        else:
            return super().event(event)

if __name__ == "__main__":
    app = QApplication()
    win = MyWidget()
    win.show()
    sys.exit(app.exec())